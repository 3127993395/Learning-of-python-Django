import copy
from django.conf import settings
from django.template.library import Library

register = Library()


@register.inclusion_tag("tag/order_menu.html")
def order_menu(request):
    # 1.读取当前用户角色信息
    # request.order_user.role
    # 2.菜单信息
    user_menu_list = copy.deepcopy(settings.ORDER_MENU[request.order_user.role])
    for item in user_menu_list:
        item['class'] = 'hide'
        for child in item['children']:
            # if child['url'] == request.path_info:     # 不合适
            if child['name'] == request.order_user.menu_name:
                child['class'] = 'active'
                item['class'] = ''

    return {'menu_list': user_menu_list}
