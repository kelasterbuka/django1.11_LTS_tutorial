from django.conf.urls import url


from . import views

urlpatterns = [
	url(r'^khusus/(?P<input>[\w-]+)$',views.khusus, name="khusus"),
	url(r'^category/$',views.categoryPost, name="category"),
	url(r'^single/$',views.singlePost, name="single"),
	url(r'^$',views.index, name="index"),
]