from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
	url(r'^contact/', include('contact.urls',namespace='contact')),
    url(r'^admin/', admin.site.urls),
]
