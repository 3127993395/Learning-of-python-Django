from django.shortcuts import render, redirect
from class_manage import models
from django import forms

from class_manage.utils.pagination import Pagination

from class_manage.utils.form import UserModelForm, ClassModelForm


def student_list(request):
    """ 学生列表 """

    info = request.session.get("info")
    if not info:
        return redirect('/login/')

    data_dict = {}
    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["phone_number"] = search_data.strip()

    queryset = models.UserInfo.objects.filter(**data_dict)
    page_object = Pagination(request, queryset)

    context = {'queryset': page_object.page_queryset, "search_data": search_data, "page_string": page_object.html()}

    return render(request, 'student_list.html', context)


def student_add(request):
    """添加学生"""
    if request.method == "GET":
        form = UserModelForm()
        return render(request, 'student_add.html', {"form": form})

    form = UserModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/student/list/')
    else:
        return render(request, 'student_add.html', {"form": form})



def student_edit(request, nid):
    """编辑学生"""
    row_object = models.UserInfo.objects.filter(id=nid).first()
    if request.method == 'GET':
        form = UserModelForm(instance=row_object)
        return render(request, 'student_edit.html', {'form': form})

    form = UserModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/student/list/')
    return redirect(request, 'student_edit.html', {'form': form})



def student_delete(request):
    """删除学生"""
    nid = request.GET.get("nid")

    models.UserInfo.objects.filter(id=nid).delete()
    return redirect('/student/list/')
