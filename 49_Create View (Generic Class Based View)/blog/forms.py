from django import forms

# model dari models.py
from .models import Artikel

class ArtikelForm(forms.ModelForm):
	class Meta:
		model = Artikel
		fields = [
			'judul',
			'isi',
			'penulis',
		]