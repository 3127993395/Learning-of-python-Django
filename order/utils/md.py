from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.utils.deprecation import MiddlewareMixin


class UserInfo(object):
    def __init__(self, role, name, id):
        self.id = id
        self.name = name
        self.role = role
        self.menu_name = None
        self.text_list = []


class AuthMiddleWare(MiddlewareMixin):

    def is_white_url(self, request):
        # 设置不需要登录就能访问的URL
        if request.path_info in settings.ORDER_VALID_URL:
            return True

    def process_request(self, request):
        """ 校验用户是否已登陆 """
        if self.is_white_url(request):
            return
        # session中获取用户信息，能获取到登录成功，未获取到则跳转到登录页面
        user_dict = request.session.get(settings.ORDER_SESSION_KEY)
        # 未登录
        if not user_dict:
            return redirect(settings.ORDER_LOGIN_URL)
        # 已登陆，后续会用到一登陆的用户信息
        # 常用方法，封装成对象

        request.order_user = UserInfo(**user_dict)

    def process_view(self, request, callback, callback_args, callback_kwargs):
        if self.is_white_url(request):
            return

        # 1.获取当前用户访问的URL
        current_name = request.resolver_match.url_name
        # 2.判断是否是公共权限
        if current_name in settings.ORDER_PERMISSION_PUBLIC:
            return
        # 3.根据用户角色获取自己所具备的所有权限
        user_permission_dict = settings.ORDER_PERMISSION[request.order_user.role]
        # 4.判断是否在自己具备的权限中
        if current_name not in user_permission_dict:
            # if request.is_ajax():     3.2版本
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':  # 4.0版本
                return JsonResponse({'status': False, 'detail': "无权访问"})
            else:
                return render(request, 'permission.html')

        # 5.有权限
        text_list = []
        text_list.append(user_permission_dict[current_name]['text'])
        menu_name = current_name
        while user_permission_dict[menu_name]['parent']:
            menu_name = user_permission_dict[menu_name]['parent']
            text = user_permission_dict[menu_name]['text']
            text_list.append(text)
        text_list.append("首页")
        text_list.reverse()

        # 5.1 设置当前菜单的值
        request.order_user.menu_name = menu_name
        # 5.2 路径导航
        request.order_user.text_list = text_list
