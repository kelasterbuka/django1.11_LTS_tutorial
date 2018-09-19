from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^post/(?P<slugInput>[\w-]+)/$', views.detailPost),
	url(r'^category/(?P<categoryInput>[\w-]+)/$', views.categoryPost),
]