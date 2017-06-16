# coding:UTF-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class TestUser(models.Model):
    name = models.CharField(verbose_name="用户名", max_length=30, unique=True)
    name_cn = models.CharField(verbose_name='中文名', max_length=30, blank=True, null=True, default='')
    password = models.CharField(verbose_name='密码', max_length=128)
    position = models.CharField(verbose_name="职位", max_length=40, blank=True, null=True, default='')
    qq = models.CharField(verbose_name="QQ号码", null=True, blank=True, max_length=20)
    phone = models.CharField(verbose_name="手机号码", max_length=15, blank=True)
    tel = models.CharField(verbose_name="办公电话", max_length=20, blank=True)
