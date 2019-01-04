from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
	url(r'^sosmed/', include('sosmed.urls',namespace='sosmed')),
    url(r'^admin/', admin.site.urls),
]
