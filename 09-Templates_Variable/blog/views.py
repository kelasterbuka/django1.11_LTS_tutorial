from django.shortcuts import render

# Create your views here.

def index(request):
	context = {
		'judul':'blog',
		'kontributor':'mario ucup',
	}
	return render(request,'blog/index.html',context)

def news(request):
	context = {
		'judul':'news',
		'kontributor':'otong',
	}
	return render(request,'blog/index.html',context)

def cerita(request):
	context = {
		'judul':'cerita',
		'kontributor':'sandra bulog',
	}
	return render(request,'blog/index.html',context)