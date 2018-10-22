from django.shortcuts import render

# Create your views here.

def khusus(request,input):
	context = {
		'judul':input,
	}

	return render(request,'blog/index.html',context)

def categoryPost(request):
	context = {
		'judul':'category post',
	}

	return render(request,'blog/index.html',context)

def singlePost(request):
	context = {
		'judul':'single post',
	}

	return render(request,'blog/index.html',context)

def index(request):
	context = {
		'judul':'home blog',
	}

	return render(request,'blog/index.html',context)