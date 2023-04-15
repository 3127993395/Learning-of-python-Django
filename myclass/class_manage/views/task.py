
from django.shortcuts import render, redirect
from class_manage import models



def task_list(request):
    queryset = models.Task.objects.all()
    name = models.Class.title
    context = {
        "name": name,
        "queryset": queryset,
    }
    return render(request, 'task_list.html', context)
