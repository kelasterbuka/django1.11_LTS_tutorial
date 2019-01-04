from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^delete/(?P<delete_id>[0-9]+)$', views.delete, name='delete'),
	url(r'^create/$',views.create, name='create'),
	url(r'^$',views.list, name='list'),
]