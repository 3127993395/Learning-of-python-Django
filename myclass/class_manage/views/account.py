from django.shortcuts import render, redirect, HttpResponse
from class_manage.utils.form import LoginForm
from class_manage import models

from class_manage.utils.code import check_code
from io import BytesIO  # 内存对象


def login(request):
    """ 登录 """
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'login.html', {"form": form})
    form = LoginForm(data=request.POST)
    if form.is_valid():
        # 验证码校验
        user_input_code = form.cleaned_data.pop('code')
        code = request.session.get('image_code', "")
        if code.upper() != user_input_code.upper():
            form.add_error("code", "验证码错误")
        # 去数据库校验用户名和密码是否正确，获取对象或None
        admin_object = models.Admin.objects.filter(**form.cleaned_data).first()
        if not admin_object:
            form.add_error("password", "用户名或密码错误")
            return render(request, 'login.html', {"form": form})
        # 网站生成随机字符串，写到用户浏览器的cookie中，再写到session中，
        request.session["info"] = {'id': admin_object.id, 'name': admin_object.username}
        # 以秒为单位，7天免登录
        request.session.set_expiry(60 * 60 * 24 * 7)

        return redirect('/admin/list/')

    return render(request, 'login.html', {"form": form})


def image_code(request):
    """ 生成图片验证码 """
    # 调用含Pillow的函数生成图片
    img, code_string = check_code()
    # 写道自己的session中（以便于后续获取验证码并校验）
    request.session['image_code'] = code_string
    # 给session设置60s超时
    request.session.set_expiry(60)

    stream = BytesIO()
    img.save(stream, 'png')
    return HttpResponse(stream.getvalue())


def logout(request):
    """ 注销 """
    request.session.clear()
    return redirect('/login/')
