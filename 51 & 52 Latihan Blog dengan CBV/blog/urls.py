from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

from .views import BlogHomeView
urlpatterns = [
	url(r'^artikel/', include('artikel.urls', namespace='artikel')),
	url(r'^$', BlogHomeView.as_view(), name='home'),
    url(r'^admin/', admin.site.urls),
]
