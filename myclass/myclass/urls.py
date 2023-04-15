"""myclass URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path
from class_manage import views
from class_manage.views import student, grade_class, admin, account, task
urlpatterns = [
    # path('admin/', admin.site.urls),
    # 班级
    path('class/list/', grade_class.class_list),
    path('class/add/', grade_class.class_add),
    path('class/delete/', grade_class.class_delete),
    path('class/<int:nid>/edit/', grade_class.class_edit),
    # 学生
    path('student/list/', student.student_list),
    path('student/add/', student.student_add),
    path('student/<int:nid>/edit/', student.student_edit),
    path('student/delete/', student.student_delete),
    # 管理员
    path('admin/list/', admin.admin_list),
    path('admin/add/', admin.admin_add),
    path('admin/<int:nid>/edit/', admin.admin_edit),
    path('admin/delete/', admin.admin_delete),
    path('admin/<int:nid>/reset/', admin.admin_reset),
    # 登录
    path('login/', account.login),
    path('image/code/', account.image_code),
    # 注销
    path('logout/', account.logout),
    # 课表
    path('task/list/', task.task_list)
]
