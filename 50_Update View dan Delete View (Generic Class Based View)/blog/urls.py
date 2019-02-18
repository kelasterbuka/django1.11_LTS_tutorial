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
	ArtikelCreateView1,
	ArtikelCreateView2,
	ArtikelUpdateView1,
	ArtikelUpdateView2,
	ArtikelDeleteView,
	)

from .models import Artikel
from .forms import ArtikelForm

urlpatterns = [
	url(r'^delete/(?P<pk>\d+)$', ArtikelDeleteView.as_view(), name='delete'),
	url(r'^update2/(?P<pk>\d+)$', ArtikelUpdateView2.as_view(), name='update2'),
	url(r'^update1/(?P<pk>\d+)$', ArtikelUpdateView1.as_view(), name='update1'),
	url(r'^create/$', ArtikelCreateView2.as_view(), name='create'),
	# url(r'^create/$', ArtikelCreateView1.as_view(), name='create'),
	# url(r'^create/$', ArtikelFormView.as_view(), name='create'),
	# url(r'^create/$', FormView.as_view(form_class=ArtikelForm, template_name='blog/create.html'), name='create'),
	url(r'^(?P<penulis>\w+)/(?P<page>\d+)$', ArtikelListView.as_view(), name='list'),
	url(r'^(?P<penulis>\w+)/$', ArtikelListView.as_view(), name='list'),
	url(r'^detail/(?P<slug>[\w-]+)$', ArtikelDetailView.as_view(model=Artikel), name='detail'),
	# url(r'^detail/(?P<slug>[\w-]+)$', DetailView.as_view(model=Artikel), name='detail'),
	# url(r'^$', ListView.as_view(model=Artikel), name = 'list'),
]