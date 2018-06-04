from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^cerita/$',views.cerita),
	url(r'^news/$',views.news),
	url(r'^$', views.index),
]