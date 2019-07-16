from django.db import models
from django.utils.text import slugify
# Create your models here.

class Artikel(models.Model):
	judul		= models.CharField(max_length=255)
	isi			= models.TextField()
	published	= models.DateTimeField(auto_now_add=True)
	updated		= models.DateTimeField(auto_now=True)
	slug		= models.SlugField(blank=True, editable=False)

	class Meta:
		default_permissions = ('add',)
		permissions = (
			('can_publish','can publish artikel'),
			('can_edit','can edit artikel')
			)

	def save(self):
		self.slug = slugify(self.judul)
		super().save()

	def __str__(self):
		return "{}.{}".format(self.id, self.judul)