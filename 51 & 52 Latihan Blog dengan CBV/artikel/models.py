from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.

class Artikel(models.Model):
	judul		= models.CharField(max_length=255)
	isi 		= models.TextField()
	kategori 	= models.CharField(max_length=255)
	published	= models.DateTimeField(auto_now_add=True)
	updated 	= models.DateTimeField(auto_now=True)
	slug		= models.SlugField(blank=True, editable=False)

	def save(self):
		self.slug = slugify(self.judul)
		super().save()

	def get_absolute_url(self):
		url_slug = {'slug':self.slug}
		return reverse('artikel:detail', kwargs = url_slug)

	def __str__(self):
		return "{}. {}".format(self.id, self.judul)