import datetime
import random

from web import models
from django.db.models import F
from django.urls import reverse
from django.shortcuts import render, redirect
from utils.pagination import Pagination
from web.forms.order import OrderModalForm
from utils.vedio import get_old_view_count
from django.conf import settings
from django_redis import get_redis_connection
from django.db import transaction

from django.contrib import messages
from django.contrib.messages.api import get_messages


def order_list(request):
    # 获取当前登录客户id
    queryset = models.Order.objects.filter(customer_id=request.order_user.id, active=1).order_by('-id')
    pager = Pagination(request, queryset)
    return render(request, 'order_list.html', {"pager": pager})


def order_add(request):
    if request.method == "GET":
        form = OrderModalForm()
        return render(request, 'form.html', {"form": form})
    form = OrderModalForm(data=request.POST)
    if not form.is_valid():
        return render(request, 'form.html', {"form": form})

    # 获取到的 URL count    # 要考虑:事务 + 锁
    video_url = form.cleaned_data['url']
    count = form.cleaned_data['count']

    # 0.发送网络请求，通过爬虫获取原播放
    status, old_view_count = get_old_view_count(video_url)
    if not status:
        form.add_error('count', "视频原播放量获取失败")
        return render(request, 'form.html', {"form": form})

    # 1.根据数量获取单价，计算出原价
    for idx in range(len(form.price_count_list) - 1, -1, -1):
        limit_count, _, unit_price = form.price_count_list[idx]
        if count >= limit_count:
            break
    total_price = count * unit_price

    # 2.找到当前的客户所处级别， 计算出折扣后价格
    try:
        with transaction.atomic():
            customer_obj = models.Customer.objects.filter(id=request.order_user.id).select_for_update().first()
            real_price = total_price * customer_obj.level.percent / 100

            # 3.判断账户余额够不够
            if customer_obj.balance < real_price:
                form.add_error('count', "账户余额不足")
                return render(request, 'form.html', {"form": form})

            # 4.创建订单
            # 4.1 随机生成订单号
            while True:
                rand_num = random.randint(10000000, 99999999)
                ctime = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
                oid = "{}{}".format(ctime, rand_num)
                exists = models.Order.objects.filter(oid=oid).exists()
                if exists:
                    continue
                break

            # 4.2 客户ID就是当前登录客户的ID       # request.order_user.id
            form.instance.oid = oid
            form.instance.price = total_price
            form.instance.real_price = real_price
            form.instance.old_view_count = old_view_count
            form.instance.customer_id = request.order_user.id
            form.save()

            # 5.账户扣款
            models.Customer.objects.filter(id=request.order_user.id).update(balance=F("balance") - real_price)

            # 6.生成交易记录
            models.TransactionRecord.objects.create(
                charge_type=3,
                customer_id=request.order_user.id,
                amount=real_price,
                order_oid=oid,
            )

            # 7.写入到redis队列中，等待执行
            conn = get_redis_connection("default")
            conn.lpush(settings.QUEUE_TASK_NAME, oid)
    except Exception:
        form.add_error('count', "创建订单失败")
        return render(request, 'form.html', {"form": form})

    return redirect(reverse("order_list"))


def order_cancel(request, pk):
    order_object = models.Order.objects.filter(id=pk, active=1, status=1, customer=request.order_user.id).first()
    if not order_object:
        messages.add_message(request, settings.MESSAGE_DANGER_TAG, "订单不存在")
        return redirect(reverse("order_list"))

    try:
        with transaction.atomic():
            customer_obj = models.Customer.objects.filter(id=request.order_user.id).select_for_update().first()
            # 1.改变订单状态(事务和锁)
            models.Order.objects.filter(id=pk, active=1, status=1, customer=request.order_user.id).update(status=5)
            # 2.归还余额
            models.Customer.objects.filter(id=request.order_user.id).update(
                balance=F("balance") + order_object.real_price)
            # 3.交易记录
            models.TransactionRecord.objects.create(
                charge_type=5,
                customer_id=request.order_user.id,
                amount=order_object.real_price,
                order_oid=order_object.oid,
            )

            messages.add_message(request, messages.SUCCESS, "撤单成功")  # 以列表形式存在
            return redirect(reverse("order_list"))
    except Exception as e:
        messages.add_message(request, settings.MESSAGE_DANGER_TAG, "撤单失败，{}".format(str(e)))
        return redirect(reverse("order_list"))


