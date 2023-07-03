# 内置模块
import random

# 第三方模块
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django_redis import get_redis_connection
from django.conf import settings

# 自定义模块
from web import models
from utils import tencent
from utils.response import BaseResponse
from web.forms.account import LoginForm, SmsLoginForm, MobileForm


class Role:
    ADMIN = "1"
    CUSTOMER = "2"


login_html = "login.html"


def login(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, login_html, {"form": form})
    # 接收并获取数据(数据格式是否为空的验证 Form组件和ModelForm组件)
    form = LoginForm(data=request.POST)
    if not form.is_valid():
        return render(request, login_html, {"form": form})

    # 去数据库校验 1 管理员   2 客户

    data_dict = form.cleaned_data
    role = data_dict.pop('role')
    if role == Role.ADMIN:
        user_object = models.Administrator.objects.filter(active=1).filter(**data_dict).first()
    else:
        user_object = models.Customer.objects.filter(active=1).filter(**data_dict).first()

    # 校验失败
    if not user_object:
        form.add_error("username", "用户名或密码错误")
        return render(request, login_html, {'form': form})

    # 校验成功，将用户信息写入session中+进入项目后台
    mapping = {Role.ADMIN: "ADMIN", Role.CUSTOMER: "CUSTOMER"}
    request.session[settings.ORDER_SESSION_KEY] = {'role': mapping[role], 'name': user_object.username,
                                                   'id': user_object.id}
    return redirect(settings.LOGIN_HOME)


def sms_send(request):
    """ 发送短信 """
    res = BaseResponse()

    # 校验数据合法性：手机号格式 + 角色
    form = MobileForm(data=request.POST)
    if not form.is_valid():
        res.detail = form.errors
        return JsonResponse(res.dict)

    res.status = True
    return JsonResponse(res.dict)


def sms_login(request):
    if request.method == "GET":
        form = SmsLoginForm()
        return render(request, "sms_login.html", {'form': form})

    res = BaseResponse()
    # 手机号格式校验
    form = SmsLoginForm(data=request.POST)
    if not form.is_valid():
        res.detail = form.errors
        return JsonResponse(res.dict)

    # 登录成功 + 注册（检测手机号是否存在）
    # 未注册，自动注册
    # 已注册，直接登录
    role = form.cleaned_data['role']
    mobile = form.cleaned_data['mobile']
    if role == Role.ADMIN:
        user_object = models.Administrator.objects.filter(active=1, mobile=mobile).first()
    else:
        user_object = models.Customer.objects.filter(active=1, mobile=mobile).first()
    if not user_object:
        res.detail = {"mobile": ["手机号不存在"]}
        return JsonResponse(res.dict)

    # 校验成功，将用户信息写入session中+进入项目后台
    mapping = {Role.ADMIN: "ADMIN", Role.CUSTOMER: "CUSTOMER"}
    request.session[settings.ORDER_SESSION_KEY] = {'role': mapping[role], 'name': user_object.username,
                                                   'id': user_object.id}
    res.status = True
    res.data = settings.LOGIN_HOME
    return JsonResponse(res.dict)


def logout(request):
    request.session.clear()
    return redirect(settings.ORDER_LOGIN_URL)


def home(request):
    return render(request, "home.html")
