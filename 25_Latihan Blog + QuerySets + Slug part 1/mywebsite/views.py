from django.shortcuts import render


def index(request):
	context = {
		'Judul':'Home Page',
		'Content':'ini adalah home page dari website ini'
	}

	return render(request,'index.html',context)