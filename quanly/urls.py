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
    url(r'^bacsi/add/$', views.bacsi_add, name='bacsi_add'),
    url(r'^bacsi/(?P<pk>\d+)/edit/$', views.bacsi_edit, name='bacsi_edit'),
    url(r'^bacsi/(?P<pk>\d+)/del/$', views.bacsi_del, name='bacsi_del'),
    url(r'^kythuatvien/$', views.kythuatvien_list, name='kythuatvien_list'),
    url(r'^kythuatvien/add/$', views.kythuatvien_add, name='kythuatvien_add'),
    url(r'^kythuatvien/(?P<pk>\d+)/edit/$', views.kythuatvien_edit, name='kythuatvien_edit'),
    url(r'^kythuatvien/(?P<pk>\d+)/del/$', views.kythuatvien_del, name='kythuatvien_del'),
    url(r'^test/$', views.test, name='test'),
    url(r'^chochut/$', views.chochut_list, name='chochut_list'),
    url(r'^benhnhan/(?P<pk>\d+)/addch/$', views.chochut_add, name='chochut_add'),
    url(r'^benhnhan/(?P<pk>\d+)/editch/$', views.chochut_edit, name='chochut_edit'),
    url(r'^benhnhan/(?P<pk>\d+)/delch/$', views.chochut_del, name='chochut_del'),
    url(r'^chuyenphoi/$', views.chuyenphoi_list, name='chuyenphoi_list'),
    url(r'^benhnhan/(?P<pk>\d+)/addcp/$', views.chuyenphoi_add, name='chuyenphoi_add'),
    url(r'^benhnhan/(?P<pk>\d+)/editcp/$', views.chuyenphoi_edit, name='chuyenphoi_edit'),
    url(r'^benhnhan/(?P<pk>\d+)/delcp/$', views.chuyenphoi_del, name='chuyenphoi_del'),
)
