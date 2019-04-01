from django.conf.urls import url


from .views import (
	ArtikelListView, 
	ArtikelDetailView,
	ArtikelKategoriListView,
	ArtikelCreateView,
	ArtikelManageView,
	ArtikelDeleteView,
	ArtikelUpdateView,
)

urlpatterns = [
	url(r'^manage/update/(?P<pk>\d+)$', ArtikelUpdateView.as_view(), name='update'),
	url(r'^manage/delete/(?P<pk>\d+)$', ArtikelDeleteView.as_view(), name='delete'),
	url(r'^manage/$', ArtikelManageView.as_view(), name='manage'),
	url(r'^tambah/$', ArtikelCreateView.as_view(), name='create'),
	url(r'^kategori/(?P<kategori>[\w]+)/(?P<page>\d+)$', ArtikelKategoriListView.as_view(), name='category'),
	url(r'^detail/(?P<slug>[\w-]+)$', ArtikelDetailView.as_view(), name='detail'),
	url(r'^(?P<page>\d+)$', ArtikelListView.as_view(), name='list'),
]