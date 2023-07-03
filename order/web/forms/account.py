import random

from django_redis import get_redis_connection
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

from web import models
from django import forms
from utils import tencent
from utils.encrypt import md5
from utils.tencent import send_sms


class Role:
    ADMIN = "1"
    CUSTOMER = "2"


class LoginForm(forms.Form):
    role = forms.ChoiceField(
        choices=(("1", "管理员"), ("2", "客户")),
        widget=forms.Select(attrs={"class": "form__title"})
    )
    # <input type="text" placeholder="用户名" class="input" name="username"/>
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "input", "placeholder": "用户名"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "input", "placeholder": "密码"})
    )

    def clean_password(self):
        return md5(self.cleaned_data['password'])


class MobileForm(forms.Form):
    role = forms.ChoiceField(
        choices=(("1", "管理员"), ("2", "客户")),
        widget=forms.Select(attrs={"class": "form__title"})
    )
    mobile = forms.CharField(
        label="手机号",
        validators=[RegexValidator(r'^1\d{10}$', '手机号格式错误')],
        required=True,
    )

    def clean_mobile(self):
        role = self.cleaned_data.get('role')
        mobile = self.cleaned_data['mobile']
        if not role:
            return mobile
        if role == Role.ADMIN:
            exists = models.Administrator.objects.filter(active=1, mobile=mobile).exists()
        else:
            exists = models.Customer.objects.filter(active=1, mobile=mobile).exists()
        if not exists:
            raise ValidationError("手机号不存在")

        # 发送短信 + 生成验证码
        sms_code = str(random.randint(1000, 9999))
        is_success = tencent.send_sms(mobile, sms_code)
        if not is_success:
            raise ValidationError("短信发送失败")

        # 将手机号和验证码保存（以便于下次进行校验） redis-->超时时间
        conn = get_redis_connection("default")
        conn.set(mobile, sms_code, ex=60)

        return mobile


class SmsLoginForm(forms.Form):
    role = forms.ChoiceField(
        choices=(("1", "管理员"), ("2", "客户")),
        widget=forms.Select(attrs={"class": "form__title"})
    )
    mobile = forms.CharField(
        validators=[RegexValidator(r'^1\d{10}$', '手机号格式错误')],
        widget=forms.TextInput(attrs={"class": "input", "placeholder": "手机号"})
    )
    code = forms.CharField(
        validators=[RegexValidator(r'^[0-9]{4}$', '验证码格式错误')],
        widget=forms.TextInput(attrs={"class": "input", "placeholder": "验证码"})
    )

    def clean_code(self):
        # 2.短信验证码 + 去redis中获取验证码
        mobile = self.cleaned_data.get('mobile')
        code = self.cleaned_data['code']
        if not mobile:
            return ''

        conn = get_redis_connection("default")
        cache_code = conn.get(mobile)
        if not cache_code:
            raise ValidationError("验证码未发送或失效")

        if code != cache_code.decode('utf-8'):
            raise ValidationError("短信验证码错误")

        return code
