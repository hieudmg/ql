from django.conf.urls import url
from . import views


urlpatterns = (
    url(r'^benhnhan/$', views.thongtin_list, name='benhnhan_list'),
    url(r'^benhnhan/add/$', views.thongtin_add, name='thongtin_add'),
    url(r'^benhnhan/(?P<pk>\d+)/edit/$', views.thongtin_edit, name='thongtin_edit'),
    url(r'^benhnhan/(?P<pk>\d+)/info/$', views.thongtin_info, name='thongtin_info'),
    url(r'^benhnhan/(?P<pk>\d+)/del/$', views.thongtin_del, name='thongtin_del'),
    url(r'^benhnhan/add/trung/$', views.trung_add, name='trung_add'),
    url(r'^bacsi/$', views.bacsi_list, name='bacsi_list'),
    url(r'^test/$', views.test, name='tese'),
)
