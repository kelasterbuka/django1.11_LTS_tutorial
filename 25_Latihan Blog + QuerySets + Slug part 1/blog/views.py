from django.shortcuts import render

# Create your views here.

from .models import Post

def index(request):
	posts = Post.objects.all();
	categories = Post.objects.values('category').distinct();
	context = {
		'Judul':'Home Blog',
		'Content':'ini adalah halaman blog',
		'Categories':categories,
		'Posts':posts,
	}

	return render(request,'blog/index.html',context)

def categoryPost(request,categoryInput):
	posts = Post.objects.filter(category=categoryInput);
	categories = Post.objects.values('category').distinct();
	context = {
		'Judul':'Home Blog',
		'Content':'tampilkan berdasarkan category',
		'Categories':categories,
		'Posts':posts,
	}

	return render(request,'blog/category.html',context)


def detailPost(request,slugInput):
	posts = Post.objects.get(slug=slugInput);
	categories = Post.objects.values('category').distinct();
	context = {
		'Judul':'Home Blog',
		'Content':'ini adalah halaman blog',
		'Categories':categories,
		'Posts':posts,
	}

	return render(request,'blog/detail.html',context)