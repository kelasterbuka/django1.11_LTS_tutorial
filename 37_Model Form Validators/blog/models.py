from django.db import models

# Create your models here.
from .validators import validate_author

class Post(models.Model):
	judul		= models.CharField(max_length = 100)
	body		= models.TextField()
	author 		= models.CharField(
		max_length = 100, 
		validators = [validate_author]
		)

	LIST_CATEGORY = (
		('Jurnal', 'jurnal'),
		('Blog', 'blog'),
		('Berita', 'berita'),
		)

	category	= models.CharField(
		max_length=100,
		choices = LIST_CATEGORY,
		default = 'Blog',
		)


	def __str__(self):
		return "{}.{}".format(self.id,self.judul)