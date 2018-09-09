from django.db import models

# Create your models here.

class Post(models.Model):
	judul = models.CharField(max_length=255)
	body = models.TextField()
	category = models.CharField(max_length=255)

	def __str__(self):
		return "{}. {}".format(self.id,self.judul)

