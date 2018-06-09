from django.shortcuts import render

def index(request):
	context = {
	 	'title':'Kelas Terbuka',
	 	'heading':'Selamat Datang',
	 	'subheading':'di kelas terbuka',
	}
	return render(request,'index.html',context)