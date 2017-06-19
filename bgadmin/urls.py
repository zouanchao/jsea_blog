# coding:UTF-8
from django.conf.urls import url

from . import views
app_name = 'bgadmin'

urlpatterns = [
    url(r'^$', views.bgadmin_home, name="bgadmin_home"),
    url(r'^import_excel/$', views.import_excel, name="import_excel"),
    url(r'^down_loda_templates/$', views.down_loda_templates, name="down_loda_templates"),
]
