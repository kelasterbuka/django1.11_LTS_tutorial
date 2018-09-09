from django.db import models

# Create your models here.

class Post(models.Model):
	judul = models.CharField(max_length=200)
	body = models.TextField()

	def __str__(self):
		return "{}".format(self.judul)