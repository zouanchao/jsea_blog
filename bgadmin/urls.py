# coding:UTF-8
from django.conf.urls import url

from . import views
app_name = 'bgadmin'

urlpatterns = [
    url(r'^bgadmin_home/$', views.bgadmin_home, name="bgadmin_home"),
    url(r'^import_excel/$', views.import_excel, name="import_excel"),
]
