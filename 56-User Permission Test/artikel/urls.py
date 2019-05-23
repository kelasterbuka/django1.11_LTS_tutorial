from django.conf.urls import url

from .views import artikelIndexView, artikelAddView, artikelAddView2, otongView

urlpatterns = [
	url(r'^otong/$', otongView, name='otong'),	
	url(r'^add2/$', artikelAddView2, name='add2'),
	url(r'^add/$', artikelAddView, name='add'),
	url(r'^$', artikelIndexView, name='index'),
]