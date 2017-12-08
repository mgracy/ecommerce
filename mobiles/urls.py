from django.conf.urls import url
from django.contrib import admin
from . import views

app_name='mobiles'
urlpatterns = [
	url(r'^$', views.index),
	url(r'^product/$', views.product_list, name='product_list'),
	url(r'^product/(?P<product_id>[0-9]+)/$', views.product_detail, name='product_detail'),
]