from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^post/(?P<slugInput>[\w-]+)/$', views.detailPost, name="detail"),
	url(r'^category/(?P<categoryInput>[\w-]+)/$', views.categoryPost, name="category"),
]