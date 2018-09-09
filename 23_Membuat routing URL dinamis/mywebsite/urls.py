from django.conf.urls import url
from django.contrib import admin

from . import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^(?P<input>[0-9]{2})/$',views.angka),
    url(r'^(?P<tahun>[0-9]{4})/(?P<bulan>[0-9]{2})/(?P<hari>[0-9]{2})/$',views.tanggal),
    url(r'^(?P<page>[\w_]+)/$',views.link),
]
