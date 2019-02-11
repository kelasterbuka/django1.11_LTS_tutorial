from django.conf.urls import url
from django.views.generic import ListView, DetailView
from .views import ArtikelListView, ArtikelDetailView
from .models import Artikel


urlpatterns = [
	url(r'^(?P<penulis>\w+)/(?P<page>\d+)$', ArtikelListView.as_view(), name='list'),
	url(r'^(?P<penulis>\w+)/$', ArtikelListView.as_view(), name='list'),
	url(r'^detail/(?P<slug>[\w-]+)$', ArtikelDetailView.as_view(model=Artikel), name='detail'),
	# url(r'^detail/(?P<slug>[\w-]+)$', DetailView.as_view(model=Artikel), name='detail'),
	# url(r'^$', ListView.as_view(model=Artikel), name = 'list'),
]