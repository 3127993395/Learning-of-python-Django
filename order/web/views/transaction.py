from django.shortcuts import render
from web import models
from utils.pagination import Pagination
from django.db.models import Q
from utils.group import Option, OrderSearchGroup


def transaction_list(request):
    search_group = OrderSearchGroup(
        request,
        models.TransactionRecord,
        Option('charge_type', db_condition={'active': 1}),
    )

    keyword = request.GET.get("keyword", "").strip()
    con = Q()
    if keyword:
        con.connector = 'OR'
        con.children.append(('order_oid__contains', keyword))

    queryset = models.TransactionRecord.objects.filter(con).filter(**search_group.get_condition).filter(
        customer_id=request.order_user.id,
        active=1)
    pager = Pagination(request, queryset)

    context = {
        'pager': pager,
        'keyword': keyword,
        'search_group': search_group,
    }
    return render(request, 'transaction_list.html', context)


def all_transaction_list(request):
    search_group = OrderSearchGroup(
        request,
        models.TransactionRecord,
        Option('charge_type', db_condition={'active': 1}),
    )

    keyword = request.GET.get("keyword", "").strip()
    con = Q()
    if keyword:
        con.connector = 'OR'
        con.children.append(('order_oid__contains', keyword))

    queryset = models.TransactionRecord.objects.filter(con).filter(**search_group.get_condition).filter(active=1)
    pager = Pagination(request, queryset)

    context = {
        'pager': pager,
        'keyword': keyword,
        'search_group': search_group,
    }
    return render(request, 'all_transaction_list.html', context)
