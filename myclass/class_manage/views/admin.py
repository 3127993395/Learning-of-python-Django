from django.shortcuts import render, redirect

from class_manage import models
from class_manage.utils.pagination import Pagination
from class_manage.utils.form import AdminModelForm, AdminEditModelForm, AdminResetModelForm


def admin_list(request):
    """管理员列表"""


    # 检查用户是否登录，若已登陆，继续，若未登录，则跳转回登录页面
    # 用户发来请求，获取随机字符串，看看session中有没有
    # 使用中间件



    # 构造搜索
    data_dict = {}
    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["username__contains"] = search_data.strip()

    # 根据搜索条件去数据库获取
    queryset = models.Admin.objects.filter(**data_dict)

    page_object = Pagination(request, queryset)
    context = {
        "queryset": page_object.page_queryset,
        "page_string": page_object.html(),
        "search_data": search_data,
    }
    return render(request, 'admin_list.html', context)


def admin_add(request):
    """添加管理员"""
    title = "新建管理员"
    if request.method == "GET":
        form = AdminModelForm()
        return render(request, 'add_edit.html', {"title": title, "form": form})

    form = AdminModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/admin/list/')
    return render(request, 'add_edit.html', {"title": title, "form": form})


def admin_edit(request, nid):
    """ 编辑管理员 """
    # 对象/ None
    row_object = models.Admin.objects.filter(id=nid).first()
    if not row_object:
        return redirect('/admin/list/')
    title = "编辑管理员"

    if request.method == "GET":
        form = AdminEditModelForm(instance=row_object)
        return render(request, 'add_edit.html', {"title": title, "form": form})

    form = AdminEditModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/admin/list/')

    return render(request, 'add_edit.html', {"title": title, "form": form})


def admin_delete(request):
    """ 删除管理员 """
    nid = request.GET.get("nid")
    models.Admin.objects.filter(id=nid).delete()
    return redirect('/admin/list/')


def admin_reset(request, nid):
    """ 重置密码 """
    # 对象/ None
    row_object = models.Admin.objects.filter(id=nid).first()
    if not row_object:
        return redirect('/admin/list/')
    title = "重置密码 - {}".format(row_object.username)
    if request.method == "GET":
        form = AdminResetModelForm()
        return render(request, 'add_edit.html', {"title": title, "form": form})
    form = AdminResetModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/admin/list/')
    return render(request, 'add_edit.html', {"title": title, "form": form})
