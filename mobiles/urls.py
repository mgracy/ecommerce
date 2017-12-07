from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
	# 'django.views.generic.list_detail',
	# url(r'^product/$', 'object_list',{'queryset': Product.objects.all()}),
	# url(r'^product/(?P<slug>[-\w]+/$', 'object_detail', {'queryset': Product.objects.all()})
	url(r'^$', views.index),
	url(r'^product/$', views.products),
]