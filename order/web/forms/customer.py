from web import models

from django import forms
from utils.bootstrap import BootStrapForm
from django.core.validators import RegexValidator


class CustomerModelForm(BootStrapForm, forms.ModelForm):
    exclude_field_list = ['level']
    confirm_password = forms.CharField(
        label="重复密码",
        widget=forms.PasswordInput(render_value=True),  # render_value=True保留原来的值
    )

    mobile = forms.CharField(
        label="手机号",
        validators=[RegexValidator(r'^1\d{10}$', '手机号格式错误')],  # 此校验也可以放在models.py中
    )

    class Meta:
        model = models.Customer
        fields = ['username', 'mobile', 'password', 'confirm_password', 'level']
        widgets = {
            'password': forms.PasswordInput(render_value=True),
            'level': forms.RadioSelect(attrs={"class": "form-radio"})
        }

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # request可能会用 print(self.fields['level'].queryset)
        self.fields['level'].queryset = models.Level.objects.filter(active=1)

    # 钩子方法判断手机号格式是否错误，等同于上文     validators=[RegexValidator(r'^1\d{10}$', '手机号格式错误')]
    # def clean_mobile(self):
    #     mobile = self.cleaned_data['mobile']
    #     import re
    #     from django.core.exceptions import ValidationError
    #     if not re.match(r'^1\d{10}$', mobile):
    #         raise ValidationError("手机号格式错误")
    #     return mobile

    def clean_password(self):
        password = self.cleaned_data.get('password')
        return md5(password)

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = md5(self.cleaned_data.get('confirm_password', ''))

        if password != confirm_password:
            raise ValidationError("密码不一致")
        return confirm_password


class CustomerEditModelForm(BootStrapForm, forms.ModelForm):
    class Meta:
        model = models.Customer
        fields = ['username', 'mobile', 'level']
        widgets = {
            'password': forms.PasswordInput(render_value=True),
        }

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # request可能会用
        self.fields['level'].queryset = models.Level.objects.filter(active=1)


class CustomerResetModelForm(BootStrapForm, forms.ModelForm):
    confirm_password = forms.CharField(
        label="重复密码",
        widget=forms.PasswordInput(render_value=True),  # render_value=True保留原来的值
    )

    class Meta:
        model = models.Customer
        fields = ['password', 'confirm_password']
        widgets = {
            'password': forms.PasswordInput(render_value=True),
        }

    def clean_password(self):
        password = self.cleaned_data.get('password')
        return md5(password)

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = md5(self.cleaned_data.get('confirm_password', ''))

        if password != confirm_password:
            raise ValidationError("密码不一致")
        return confirm_password


class ChargeModelForm(BootStrapForm, forms.ModelForm):
    # 静态变量
    # charge_type = forms.TypedChoiceField(
    #     label="类型",
    #     choices=[(1, "充值"), (2, "扣款")],   # 只适合固定的数据，不要从数据库的表里获取数据
    #     coerce=int,
    # )

    class Meta:
        model = models.TransactionRecord
        fields = ['charge_type', 'amount']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['charge_type'].choices = [(1, "充值"), (2, "扣款")]


