from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect

class AuthMiddleware(MiddlewareMixin):
    """ 中间件 """

    def process_request(self, request):

        # 0.排除不需要登录就能访问的页面
        # request.path_info获取当前用户访问的URL
        if request.path_info in ["/login/", "/image/code/"]:
            return

        # 1.读取当前用户访问的session信息。如果能得到，说明已登录过
        info_dict = request.session.get("info")
        if info_dict:
            return
        # 2.如果没有登录信息，回到登录页面
        return redirect('/login/')