from django.db import models

# Create your models here.

class PostModel(models.Model):
	judul		= models.CharField(max_length = 20)
	body		= models.TextField()
	category	= models.CharField(max_length = 20)

	published	= models.DateTimeField(auto_now_add = True)
	updated		= models.DateTimeField(auto_now = True)

	def __str__(self):
		return "{}. {}".format(self.id, self.judul)