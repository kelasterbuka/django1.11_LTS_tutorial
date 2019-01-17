from django.conf.urls import url
from django.contrib import admin
from django.views.generic.base import TemplateView

from .views import IndexView, ContextView, ParameterView

urlpatterns = [
	url(r'^parameter/(?P<parameter1>[0-9]+)/(?P<parameter2>[0-9]+)$', ParameterView.as_view()),
	url(r'^context$', ContextView.as_view()),
	url(r'^default$', TemplateView.as_view(template_name='default.html')),
	url(r'^$', IndexView.as_view(template_name='index.html')),
    url(r'^admin/', admin.site.urls),
]


# 1. membuat class view di views.py, tapi menggunakan templatenya di url
# 2. jika halaman kita itu statis, tidak ada perubahan apapaun,
#    maka kita lakukan templateview langsung pada urls.py
# 3. Membuat views dengan context saja, kita menggunakan class
#    templateview di views.py
# 4. Kita memasukan parameter kedalam template, dengan menggunakan regex
