from web import models
from django.urls import reverse
from django.shortcuts import render, redirect

from utils.link import filter_reverse
from web.forms.level import LevelModelForm


def level_list(request):
    queryset = models.Level.objects.filter(active=1)
    return render(request, 'level_list.html', {"queryset": queryset})


def level_add(request):
    if request.method == "GET":
        form = LevelModelForm()
        return render(request, 'form.html', {"form": form})
    form = LevelModelForm(data=request.POST)
    if not form.is_valid():
        return render(request, 'form.html', {"form": form})
    form.save()
    return redirect(reverse('level_list'))


def level_edit(request, pk):
    level_object = models.Level.objects.filter(id=pk, active=1).first()
    if request.method == "GET":
        form = LevelModelForm(instance=level_object)
        return render(request, 'form.html', {"form": form})

    # 获取数据 + 校验
    form = LevelModelForm(data=request.POST, instance=level_object)
    if not form.is_valid():
        return render(request, 'form.html', {"form": form})

    # 根据用户提交是数据进行更新
    form.save()
    return redirect(filter_reverse(request, reverse('level_list')))


def level_delete(request, pk):
    exists = models.Customer.objects.filter(level_id=pk).exists()
    if not exists:
        models.Level.objects.filter(id=pk).update(active=0)
    return redirect(reverse('level_list'))
