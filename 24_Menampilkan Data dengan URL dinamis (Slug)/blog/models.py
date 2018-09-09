from django.db import models
from django.utils.text import slugify
# Create your models here.

class Post(models.Model):
	judul = models.CharField(max_length=255)
	body = models.TextField()
	category = models.CharField(max_length=255)
	slug = models.SlugField(blank=True,editable=False)

	def save(self):
		self.slug = slugify(self.judul)
		super(Post, self).save()

	def __str__(self):
		return "{}. {}".format(self.id,self.judul)

