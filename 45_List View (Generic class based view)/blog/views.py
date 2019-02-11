from django.shortcuts import render

from django.views.generic import ListView

from .models import Artikel

class ArtikelListView(ListView):
	model = Artikel
	ordering = ['update']
	extra_context = {
		'page_title':'Blog List',
	}

	def get_context_data(self,*args,**kwargs):
		self.kwargs.update(self.extra_context)
		kwargs = self.kwargs
		print(kwargs)
		return super().get_context_data(*args,**kwargs)


def index(request):

	context = {
		'page_title':'Blog',
	}

	return render(request,'blog/index.html',context)