from django.conf.urls import url, include
from django.contrib import admin

from .views import index, loginView, logoutView

urlpatterns = [
	url(r'^artikel/', include('artikel.urls',namespace='artikel')),
	url(r'^logout/$', logoutView, name="logout"),
	url(r'^login/$', loginView, name="login"),
    url(r'^$', index, name="index"),
    url(r'^admin/', admin.site.urls),
]
