from django.shortcuts import render

# Create your views here.

from .models import Post

def index(request):
	posts = Post.objects.all();
	context = {
		'Title':'Blog',
		'Heading':'Selamat Datang di Blog',
		'Category':'All',
		'Posts':posts,
	}

	return render(request,'index.html',context)

def jurnal(request):
	posts = Post.objects.filter(category='jurnal');
	context = {
		'Title':'Blog',
		'Heading':'Selamat Datang di Blog',
		'Category':'Jurnal',
		'Posts':posts,
	}

	return render(request,'index.html',context)

def berita(request):
	posts = Post.objects.filter(category='berita');
	context = {
		'Title':'Blog',
		'Heading':'Selamat Datang di Blog',
		'Category':'Berita',
		'Posts':posts,
	}

	return render(request,'index.html',context)

def gosip(request):
	posts = Post.objects.filter(category='gosip');
	context = {
		'Title':'Blog',
		'Heading':'Selamat Datang di Blog',
		'Category':'Gosip',
		'Posts':posts,
	}

	return render(request,'index.html',context)