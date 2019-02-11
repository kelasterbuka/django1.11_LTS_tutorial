from django.conf.urls import url
from django.views.generic import (
	ListView, 
	DetailView, 
	FormView
	)
from .views import (
	ArtikelListView, 
	ArtikelDetailView,
	ArtikelFormView,
	)

from .models import Artikel
from .forms import ArtikelForm

urlpatterns = [
	url(r'^create/$', ArtikelFormView.as_view(), name='create'),
	# url(r'^create/$', FormView.as_view(form_class=ArtikelForm, template_name='blog/create.html'), name='create'),
	url(r'^(?P<penulis>\w+)/(?P<page>\d+)$', ArtikelListView.as_view(), name='list'),
	url(r'^(?P<penulis>\w+)/$', ArtikelListView.as_view(), name='list'),
	url(r'^detail/(?P<slug>[\w-]+)$', ArtikelDetailView.as_view(model=Artikel), name='detail'),
	# url(r'^detail/(?P<slug>[\w-]+)$', DetailView.as_view(model=Artikel), name='detail'),
	# url(r'^$', ListView.as_view(model=Artikel), name = 'list'),
]