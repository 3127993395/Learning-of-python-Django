from django.shortcuts import render, redirect
from class_manage import models
from django import forms

from class_manage.utils.pagination import Pagination

from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from class_manage.utils.encrypt import md5


# from class_manage.utils.bootstrap import BootstrapModelForm

class ClassModelForm(forms.ModelForm):
    class Meta:
        model = models.Class
        fields = '__all__'

        # def __init__(self, *args, **kwargs):
        #     super().__init__(*args, **kwargs)


class UserModelForm(forms.ModelForm):
    """学生表单"""

    # 验证方式一
    # name = forms.CharField(min_length=2, label="姓名")
    # phone_number = forms.CharField(
    #     label="手机号",
    #     validators=[RegexValidator(r'^1[34578]\d{9}$','手机号格式错误')]
    # )

    class Meta:
        model = models.UserInfo
        fields = '__all__'

        widgets = {
            "number": forms.TextInput(attrs={"class": "form-control"}),
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "dormitory_number": forms.TextInput(attrs={"class": "form-control"}),
            "phone_number": forms.TextInput(attrs={"class": "form-control"}),
            "gender": forms.ChoiceField()
        }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #
    #     for name, field in self.fields.items():
    #         if field.widgets.attrs:
    #             field.widgets.attrs["class"] = "form-control"
    #             field.widgets.attrs["placeholder"] = field.labels
    #         else:
    #             field.widgets.attrs = {
    #                 "class": "form-control",
    #                 "placeholder": field.labels,
    #             }

    # 简化:
    # from class_manage.utils.bootstrap import BootstrapModelForm
    # class UserModleForm(BootstrapModleForm):
    #     class Meta:
    #         model = models.UserInfo
    #         fields = '__all__'

    # 验证方式二
    def clean_phone_number(self):
        txt_phone_number = self.cleaned_data['phone_number']
        if len(txt_phone_number) != 11:
            # 验证不通过
            raise ValidationError("手机号错误")
        # 验证通过，返回用户输入的值
        return txt_phone_number


class AdminModelForm(forms.ModelForm):
    confirm_password = forms.CharField(
        label="确认密码",
        widget=forms.PasswordInput(render_value=True)
    )

    class Meta:
        model = models.Admin
        fields = ["username", "password", "confirm_password"]
        widgets = {
            "password": forms.PasswordInput(render_value=True)
        }

    def clean_password(self):
        password = self.cleaned_data.get("password")
        return md5(password)

    def clean_confirm_password(self):
        password = self.cleaned_data.get("password")
        confirm_password = md5(self.cleaned_data.get("confirm_password"))
        if password != confirm_password:
            raise ValidationError("密码不一致")
        return confirm_password
        # 解释：return什么值，什么值就会导入数据库


class AdminEditModelForm(forms.ModelForm):
    class Meta:
        model = models.Admin
        fields = ['username']


class AdminResetModelForm(forms.ModelForm):
    confirm_password = forms.CharField(
        label="确认密码",
        widget=forms.PasswordInput(render_value=True)
    )

    class Meta:
        model = models.Admin
        fields = ['password', 'confirm_password']
        widgets = {
            "password": forms.PasswordInput(render_value=True)
        }

    def clean_password(self):
        password = self.cleaned_data.get("password")
        md5_password = password

        # 去数据库校验，当前输入密码和新输入密码是否一致
        exisis = models.Admin.objects.filter(id=self.instance.pk, password=md5_password).exists()
        if exisis:
            raise ValidationError("密码不能与之前一致")
        return md5_password

    def clean_confirm_password(self):
        password = self.cleaned_data.get("password")
        confirm_password = md5(self.cleaned_data.get("confirm_password"))
        if password != confirm_password:
            raise ValidationError("密码不一致")
        return confirm_password
        # 解释：return什么值，什么值就会导入数据库


class LoginForm(forms.Form):
    username = forms.CharField(
        label="用户名",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )
    password = forms.CharField(
        label="密码",
        widget=forms.PasswordInput(attrs={"class": "form-control"}, render_value=True),
    )
    code = forms.CharField(
        label="验证码",
        widget=forms.TextInput,
        required=True,
    )

    def clean_password(self):
        password = self.cleaned_data.get("password")
        return md5(password)
