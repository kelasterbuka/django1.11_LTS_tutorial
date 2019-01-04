from django.shortcuts import render

from .forms import ContactForm

def index(request):
	context = {
		'heading':'Contact Page',
		'contact_form': ContactForm,
	}

	print(request.POST)

	return render(request,'contact/index.html',context)