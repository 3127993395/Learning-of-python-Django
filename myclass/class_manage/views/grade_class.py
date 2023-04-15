from django.shortcuts import render, redirect
from class_manage import models
from django import forms
from class_manage.utils.form import UserModelForm, ClassModelForm



def class_list(request):
    """ 班级列表 """
    queryset = models.Class.objects.all()
    return render(request, 'class_list.html', {'queryset': queryset})


def class_add(request):
    """ 添加班级 """
    if request.method == 'GET':
        return render(request, 'class_add.html')
    title = request.POST.get("title")
    models.Class.objects.create(title=title)
    return redirect("/class/list")


def class_delete(request):
    """ 删除班级 """
    nid = request.GET.get("nid")

    models.Class.objects.filter(id=nid).delete()
    return redirect('/class/list/')


def class_edit(request, nid):
    """编辑班级"""
    row_object = models.Class.objects.filter(id=nid).first()
    if request.method == 'GET':
        form = ClassModelForm(instance=row_object)
        return render(request, 'class_edit.html', {'form': form})

    form = ClassModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/class/list/')
    return redirect(request, 'class_edit.html', {'form': form})