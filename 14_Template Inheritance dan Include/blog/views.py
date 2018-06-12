from django.shortcuts import render

# Create your views here.

def index(request):
	context = {
		'title':'Blog',
		'heading':'Blog',
		'subheading':'jurnal kelas terbuka',
	}
	return render(request, 'blog/index.html',context)