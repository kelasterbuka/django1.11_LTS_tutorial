from django import forms

class ContactForm(forms.Form):
	nama 	= forms.CharField()
	alamat 	= forms.CharField()
