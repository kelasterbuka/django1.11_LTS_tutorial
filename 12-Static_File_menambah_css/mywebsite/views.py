from django.shortcuts import render

def index(request):
	context = {
		'judul':'Kelas Terbuka',
		'subjudul':'selamat datang',
		'banner':'img/banner_home.png',
	}
	return render(request,'index.html',context)