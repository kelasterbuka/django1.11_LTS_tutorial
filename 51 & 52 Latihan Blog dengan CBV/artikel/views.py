from django.shortcuts import render
from django.views.generic import (
	ListView, 
	DetailView, 
	CreateView, 
	DeleteView, 
	UpdateView
)
from django.urls import reverse_lazy

# load model
from .models import Artikel
from .forms import ArtikelForm


class ArtikelUpdateView(UpdateView):
	form_class = ArtikelForm
	model = Artikel
	template_name = "artikel/artikel_update.html"


class ArtikelDeleteView(DeleteView):
	model = Artikel
	template_name = "artikel/artikel_delete_confirmation.html"
	success_url = reverse_lazy('artikel:manage')


class ArtikelManageView(ListView):
	model = Artikel
	template_name = "artikel/artikel_manage.html"
	context_object_name = 'artikel_list'


class ArtikelCreateView(CreateView):
	form_class = ArtikelForm
	template_name = "artikel/artikel_create.html"


class ArtikelPerKategori():
	model = Artikel

	def get_latest_artikel_each_kategori(self):
		kategori_list = self.model.objects.values_list('kategori', flat=True).distinct()
		queryset = []

		for kategori in kategori_list:
			artikel = self.model.objects.filter(kategori=kategori).latest('published')
			queryset.append(artikel)

		return queryset
		

class ArtikelKategoriListView(ListView):
	model = Artikel
	template_name = "artikel/artikel_kategori_list.html"
	context_object_name = 'artikel_list'
	ordering = ['-published']
	paginate_by = 3

	def get_queryset(self):
		self.queryset = self.model.objects.filter(kategori=self.kwargs['kategori'])
		return super().get_queryset()

	def get_context_data(self,*args,**kwargs):
		kategori_list = self.model.objects.values_list('kategori', flat=True).distinct().exclude(kategori=self.kwargs['kategori'])
		self.kwargs.update({'kategori_list':kategori_list})
		kwargs = self.kwargs
		return super().get_context_data(*args,**kwargs)	


class ArtikelListView(ListView):
    model = Artikel
    template_name = "artikel/artikel_list.html"
    context_object_name = 'artikel_list'
    ordering = ['-published']
    paginate_by = 3

    def get_context_data(self,*args,**kwargs):
    	kategori_list = self.model.objects.values_list('kategori', flat=True).distinct()
    	self.kwargs.update({'kategori_list':kategori_list})
    	kwargs = self.kwargs
    	return super().get_context_data(*args,**kwargs)


class ArtikelDetailView(DetailView):
	model = Artikel
	template_name = "artikel/artikel_detail.html"
	context_object_name = 'artikel'

	def get_context_data(self,*args,**kwargs):
		kategori_list = self.model.objects.values_list('kategori', flat=True).distinct()
		self.kwargs.update({'kategori_list':kategori_list})

		artikel_serupa = self.model.objects.filter(kategori=self.object.kategori).exclude(id=self.object.id)
		self.kwargs.update({'artikel_serupa':artikel_serupa})	

		kwargs = self.kwargs
		return super().get_context_data(*args,**kwargs)

