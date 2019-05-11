from django.conf.urls import url
from django.contrib import admin

from .views import index, IndexView, loginView, logoutView

urlpatterns = [
	url(r'^logout/$', logoutView, name="logout"),
	url(r'^login/$', loginView, name="login"),
	# url(r'^$', IndexView.as_view(), name="index"),
    url(r'^$', index, name="index"),
    url(r'^admin/', admin.site.urls),
]
