from django.shortcuts import render

from .forms import ContactForm

def index(request):
	contact_form = ContactForm()
	context = {
		'heading':'Contact Page',
		'contact_form': contact_form,
	}

	return render(request,'contact/index.html',context)