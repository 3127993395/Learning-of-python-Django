import copy
from django.urls import reverse
from django.conf import settings
from django.http import QueryDict
from django.template.library import Library
from django.utils.safestring import mark_safe

register = Library()


def check_permission(request, name):
    # 1.获取权限字典
    role = request.order_user.role

    # 2.根据用户角色判断所属权限 name->"customer_add"
    permission_dict = settings.ORDER_PERMISSION[role]

    if name in permission_dict:
        return True

    if name in settings.ORDER_PERMISSION_PUBLIC:
        return True

    return False


@register.simple_tag
def add_permission(request, name, *args, **kwargs):
    # 3.判断权限是否有customer_add,无权限，返回空;有权限，通过"customer_add"反向生成URL
    if not check_permission(request, name):
        return ""
    url = reverse(name, args=args, kwargs=kwargs)
    tpl = """
    <a class="btn btn-success" href="{}"><span class="glyphicon glyphicon-plus-sign"></span>新建</a>
    """.format(url)
    return mark_safe(tpl)


@register.simple_tag
def edit_permission(request, name, *args, **kwargs):
    # 3.判断权限是否有customer_edit,无权限，返回空;有权限，通过"customer_add"反向生成URL
    if not check_permission(request, name):
        return ""
    url = reverse(name, args=args, kwargs=kwargs)

    param = request.GET.urlencode()
    if param:
        new_query_dict = QueryDict(mutable=True)
        new_query_dict['_filter'] = param
        filter_string = new_query_dict.urlencode()  # new_query_dict.urlencode() 自动进行URL转义
        tpl = """<a class="btn btn-primary btn-xs" href="{}?{}">编辑</a>""".format(url, filter_string)
        return mark_safe(tpl)

    tpl = """<a class="btn btn-primary btn-xs" href="{}">编辑</a>""".format(url)
    return mark_safe(tpl)


@register.simple_tag
def delete_permission(request, name, *args, **kwargs):
    # 3.判断权限是否有customer_add,无权限，返回空;有权限，通过"customer_add"反向生成URL
    if not check_permission(request, name):
        return ""
    pk = kwargs.get('pk')
    tpl = """
    <a class="btn btn-danger btn-xs btn-delete" cid="{}">删除</a>
    """.format(pk)
    return mark_safe(tpl)


@register.simple_tag
def delete_url_permission(request, name, *args, **kwargs):
    # 3.判断权限是否有customer_add,无权限，返回空;有权限，通过"customer_add"反向生成URL
    if not check_permission(request, name):
        return ""
    url = reverse(name, args=args, kwargs=kwargs)
    tpl = """
    <a class="btn btn-danger btn-xs btn-delete" href="{}">删除</a>
    """.format(url)
    return mark_safe(tpl)


@register.filter
def has_permission(request, others):
    name_list = others.split(',')
    for name in name_list:
        status = check_permission(request, name)
        if status:
            return True
    return False
