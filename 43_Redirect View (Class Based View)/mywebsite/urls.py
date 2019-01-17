from django.conf.urls import url
from django.contrib import admin

from django.views.generic.base import TemplateView, RedirectView

from .views import HomeView, HomeRedirectView, HomeUserView

urlpatterns = [
	url(r'^home/$', HomeView.as_view(), name='home_view'),
	url(r'^rumah$', RedirectView.as_view(pattern_name='index'), name='rumah'),
	url(r'^home$', RedirectView.as_view(url='/'), name='home'),
	url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^home/(?P<user>[\w]+)$', HomeRedirectView.as_view(), name='home_redirect'),
    url(r'(?P<user>[\w]+)$', HomeUserView.as_view(), name='user'),
]
