from django.urls import reverse
from django.http import JsonResponse
from django.shortcuts import render, redirect

from web import models
from utils.link import filter_reverse
from utils.pagination import Pagination
from utils.response import BaseResponse
from web.forms.policy import PolicyModelForm


def policy_list(request):
    queryset = models.PricePolicy.objects.all().order_by('count')
    pager = Pagination(request, queryset)
    return render(request, 'policy_list.html', {"pager": pager})


def policy_add(request):
    if request.method == "GET":
        form = PolicyModelForm()
        return render(request, 'form2.html', {'form': form})
    form = PolicyModelForm(data=request.POST)
    if not form.is_valid():
        return render(request, 'form2.html', {'form': form})
    form.save()
    return redirect(reverse("policy_list"))


def policy_edit(request, pk):
    instance = models.PricePolicy.objects.filter(id=pk).first()
    if request.method == "GET":
        form = PolicyModelForm(instance=instance)
        return render(request, 'form2.html', {'form': form})
    form = PolicyModelForm(data=request.POST, instance=instance)
    if not form.is_valid():
        return render(request, 'form2.html', {'form': form})
    form.save()
    return redirect(filter_reverse(request, reverse('policy_list')))


def policy_delete(request):
    res = BaseResponse(status=True)
    cid = request.GET.get('cid')
    models.PricePolicy.objects.filter(id=cid).delete()
    return JsonResponse(res.dict)
