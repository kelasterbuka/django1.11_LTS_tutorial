from django.shortcuts import render

def index(request):
	context = {
		'judul':'kelas terbuka asoy',
		'kontributor':'faqihza',
	}
	return render(request,'index.html', context)
