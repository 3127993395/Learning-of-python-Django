from web import models

from django.db.models import Q
from django.urls import reverse
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError

from utils.encrypt import md5
from utils.link import filter_reverse
from utils.pagination import Pagination
from utils.response import BaseResponse
from utils.group import Option, OrderSearchGroup
from web.forms.customer import CustomerModelForm, CustomerEditModelForm, CustomerResetModelForm, ChargeModelForm


def customer_list(request):

    search_group = OrderSearchGroup(
        request,
        models.Customer,
        Option('level'),
    )

    keyword = request.GET.get("keyword", "").strip()
    con = Q()
    if keyword:
        con.connector = 'OR'
        con.children.append(('username__contains', keyword))
        con.children.append(('mobile__contains', keyword))
        con.children.append(('level__title__contains', keyword))

    # 所有数据
    queryset = models.Customer.objects.filter(con).filter(active=1).filter(**search_group.get_condition).select_related('level', 'creator')
    # select_related 主动连表，减少SQL语句查询次数，前端row.level.percent跨表时使用

    pager = Pagination(request, queryset)  # 分页类

    context = {
        "queryset": queryset[pager.start:pager.end],
        "pager_string": pager.html(),
        "search_group" : search_group,
    }
    return render(request, 'customer_list.html', context)


def customer_add(request):
    if request.method == "GET":
        form = CustomerModelForm(request)
        return render(request, 'form2.html', {"form": form})

    form = CustomerModelForm(request, data=request.POST)
    if not form.is_valid():
        return render(request, 'form2.html', {"form": form})

    form.instance.creator_id = request.order_user.id
    form.save()
    return redirect(reverse("customer_list"))


def customer_edit(request, pk):
    instance = models.Customer.objects.filter(id=pk, active=1).first()
    if request.method == "GET":
        form = CustomerEditModelForm(request, instance=instance)
        return render(request, 'form2.html', {'form': form})

    form = CustomerEditModelForm(request, instance=instance, data=request.POST)
    if not form.is_valid():
        return render(request, 'form2.html', {'form': form})
    form.save()
    return redirect(filter_reverse(request, reverse("customer_list")))


def customer_reset(request, pk):
    instance = models.Customer.objects.filter(id=pk, active=1).first()
    if request.method == "GET":
        form = CustomerResetModelForm(instance=instance)
        return render(request, 'form2.html', {"form": form})

    form = CustomerResetModelForm(data=request.POST, instance=instance)
    if not form.is_valid():
        return render(request, 'form2.html', {"form": form})
    form.save()
    return redirect(reverse("customer_list"))


def customer_delete(request):
    cid = request.GET.get('cid', 0)
    if not cid:
        res = BaseResponse(status=False, detail="请选择要删除的数据")
        return JsonResponse(res.dict)

    exists = models.Customer.objects.filter(id=cid, active=1).exists()
    if not exists:
        res = BaseResponse(status=False, detail="要删除的数据不存在")
        return JsonResponse(res.dict)

    models.Customer.objects.filter(id=cid, active=1).update(active=0)
    res = BaseResponse(status=True)
    return JsonResponse(res.dict)


def customer_charge(request, pk):
    queryset = models.TransactionRecord.objects.filter(customer_id=pk, customer__active=1, active=1).order_by('-id')
    pager = Pagination(request, queryset)

    form = ChargeModelForm()
    # return render(request, 'customer_charge.html', {"pager": pager, "form": form, "pk": pk})
    # locals()    获取局部变量中所有值
    return render(request, 'customer_charge.html', locals())


def customer_charge_add(request, pk):
    form = ChargeModelForm(data=request.POST)
    if not form.is_valid():
        return JsonResponse({'status': False, 'detail': form.errors})

    # 0.表单验证成功，获取数据
    amount = form.cleaned_data['amount']
    charge_type = form.cleaned_data['charge_type']

    try:
        with transaction.atomic():  # 事务 数据库用innodb引擎, 默认支持

            # 1.对当前用户进行更新，账户余额增加/减少
            # 获取相应对象的同时获取一个排他锁 select_for_update() 事务结束，锁结束
            customer_obj = models.Customer.objects.filter(id=pk, active=1).select_for_update().first()
            if charge_type == 2 and customer_obj.balance < amount:
                return JsonResponse(
                    {"status": False,
                     'detail': {"amount": ["余额不足, 账户总余额只有{}".format(customer_obj.balance)]}})

            if charge_type == 1:
                customer_obj.balance = customer_obj.balance + amount
            else:
                customer_obj.balance = customer_obj.balance - amount
            customer_obj.save()

            # 2.生成交易记录，并保存至表
            form.instance.customer = customer_obj
            form.instance.creator_id = request.order_user.id
            form.save()

    except Exception:
        return JsonResponse(
            {"status": False, 'detail': {"amount": ["操作失败"]}})

    return JsonResponse({"status": True})
