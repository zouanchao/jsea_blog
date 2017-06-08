# coding:UTF-8
from django.conf.urls import url
from django.contrib import admin
from blog.views import *

app_name = 'blog'

urlpatterns = [
    url(r'^detail/(\d+)/$',get_details,name='blog_get_detail'),
]