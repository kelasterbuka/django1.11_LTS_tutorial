from django.shortcuts import render


def index(request):
	context = {
		'heading':'Home',
	}

	if request.method == 'POST':
		print("ini adalah method post")
		context['nama'] = request.POST['nama']
		context['alamat'] = request.POST['alamat']
	else:
		print("ini adalah method get")

	return render(request, 'index.html', context)