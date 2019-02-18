from django.shortcuts import render
from django.urls import reverse_lazy


from django.views.generic import (
	ListView, 
	DetailView,
	FormView,
	CreateView,
	UpdateView,
	DeleteView,
	)

from .models import Artikel
from .forms import ArtikelForm


class ArtikelDeleteView(DeleteView):
	model = Artikel
	# template_name = 'blog/delete_konfirmasi.html'
	success_url = reverse_lazy('blog:list',kwargs={'penulis':'all'})


class ArtikelUpdateView2(UpdateView):
	model = Artikel
	fields = [
		'isi',
	]

	extra_context = {
		'page_title':'update Artikel dengan update view 2',
	}

	def get_context_data(self, *args, **kwargs):
		kwargs.update(self.extra_context)
		return super().get_context_data(*args, **kwargs)


class ArtikelUpdateView1(UpdateView):
	form_class = ArtikelForm
	model = Artikel
	template_name = 'blog/create.html'

	extra_context = {
		'page_title':'update Artikel dengan update view 1',
	}

	def get_context_data(self, *args, **kwargs):
		kwargs.update(self.extra_context)
		return super().get_context_data(*args, **kwargs)

class ArtikelCreateView2(CreateView):
	model = Artikel
	fields = [
		'judul',
		'isi',
		'penulis',
	]

	# template akan diambil dari artikel_form, suffix = _form

	extra_context = {
		'page_title':'Tambah Artikel dengan create view',
	}

	def get_context_data(self, *args, **kwargs):
		kwargs.update(self.extra_context)
		return super().get_context_data(*args, **kwargs)


class ArtikelCreateView1(CreateView):
	form_class = ArtikelForm
	template_name = 'blog/create.html'

	extra_context = {
		'page_title':'Tambah Artikel dengan create view',
	}

	def get_context_data(self, *args, **kwargs):
		kwargs.update(self.extra_context)
		return super().get_context_data(*args, **kwargs)


class ArtikelFormView(FormView):
	form_class = ArtikelForm
	template_name = 'blog/create.html'
	# success_url = '/blog/all/'
	success_url = reverse_lazy('blog:list',kwargs={'penulis':'all'})
	extra_context = {
		'page_title':'Tambah Artikel',
	}

	def get_context_data(self,*args,**kwargs):
		kwargs.update(self.extra_context)
		return super().get_context_data(*args,**kwargs)

	def form_valid(self,form):
		# print(form.cleaned_data)
		form.save()
		return super().form_valid(form)


class ArtikelDetailView(DetailView):
	model = Artikel
	extra_context = {
		'page_title':'Detail Artikel',
	}

	def get_context_data(self, *args, **kwargs):
		self.kwargs.update(self.extra_context)
		artikel_lain = self.model.objects.exclude(slug=self.kwargs['slug'])
		self.kwargs.update({'artikel_lain':artikel_lain})
		kwargs = self.kwargs
		print(kwargs)
		return super().get_context_data(*args,**kwargs)



class ArtikelListView(ListView):
	model = Artikel
	ordering = ['publish']
	# paginate_by = 2
	extra_context = {
		'page_title':'Blog List',
	}

	def get_queryset(self):
		if self.kwargs['penulis'] != 'all':
			self.queryset = self.model.objects.filter(penulis__iexact = self.kwargs['penulis'])
			self.kwargs.update({
				'penulis':self.kwargs['penulis'],
				})
		return super().get_queryset()

	def get_context_data(self,*args,**kwargs):
		self.kwargs.update(self.extra_context)
		kwargs = self.kwargs
		return super().get_context_data(*args,**kwargs)