from django.db import models

# Create your models here.
class Class(models.Model):
    """班级表"""
    title = models.CharField(verbose_name="班级",max_length=32)

    def __str__(self):
        return self.title


class UserInfo(models.Model):
    """每班学生表"""
    number = models.CharField(verbose_name="学号", max_length=16)
    name = models.CharField(verbose_name="姓名", max_length=16)

    gender_choices = (
        (1, "男"),
        (2, "女"),
    )
    gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choices)

    phone_number = models.CharField(verbose_name="联系电话", max_length=64)

    dormitory_number= models.CharField(verbose_name="宿舍编号", max_length=64)


class Admin(models.Model):
    """管理员"""
    username = models.CharField(verbose_name="用户名", max_length=32)
    password = models.CharField(verbose_name="密码", max_length=64)

class Task(models.Model):
    """ 课表管理 """
    time = models.CharField(verbose_name="时间", max_length=32)
    tuesday = models.CharField(verbose_name="周二", max_length=128)
    monday = models.CharField(verbose_name="周一", max_length=128)
    wednesday = models.CharField(verbose_name="周三", max_length=128)
    thursday = models.CharField(verbose_name="周四", max_length=128)
    friday = models.CharField(verbose_name="周五", max_length=128)
    sunday = models.CharField(verbose_name="周六", max_length=128)
    saturday = models.CharField(verbose_name="周日", max_length=128)

