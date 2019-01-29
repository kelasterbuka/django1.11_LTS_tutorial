from django.conf.urls import url

from .views import (
	SosmedListView,
	SosmedDeleteView,
	SosmedFormView,
	)
	

urlpatterns = [
	url(r'^delete/(?P<delete_id>[0-9]+)$', SosmedDeleteView.as_view(), name='delete'),
	url(r'^update/(?P<update_id>[0-9]+)$', SosmedFormView.as_view(mode='update'), name='update'),
	url(r'^create/$', SosmedFormView.as_view(), name='create'),
	url(r'^$', SosmedListView.as_view(), name='list'),
]