from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
	url(r'^', include('blog.urls', namespace = 'blog')),
    url(r'^admin/', admin.site.urls),
]
