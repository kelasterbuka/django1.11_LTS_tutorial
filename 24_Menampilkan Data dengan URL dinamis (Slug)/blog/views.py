from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import Post

def index(request):

	print(Post.objects.all())
	return HttpResponse("testing")

def categoryPost(request, categoryInput):
	posts = Post.objects.filter(category=categoryInput)
	context = {
		'Title':'Blog Posts',
		'Category':categoryInput,
		'Posts':posts,
	}

	return render(request,'/blog/categoryPost.html',context)

def singlePost(request, slugInput):
	post = Post.objects.get(slug=slugInput)
	context = {
		'test':'test'
	}
	judul = "<h1>{}</h1>".format(post.judul)
	body = "<p>{}</p>".format(post.body)
	category = "<p>{}</p>".format(post.category)
	
	return HttpResponse(judul + body + category)
