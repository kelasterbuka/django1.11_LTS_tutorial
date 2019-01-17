from django.conf.urls import url
from django.contrib import admin

from .views import index, IndexClassView

urlpatterns = [
	url(r'^$', index,name='home'),
	url(r'^class$', IndexClassView.as_view(template_name='index.html'), name='home-class'),
	url(r'^class2$', IndexClassView.as_view(template_name='index2.html'), name='home-class2'),
    url(r'^admin/', admin.site.urls),
]
