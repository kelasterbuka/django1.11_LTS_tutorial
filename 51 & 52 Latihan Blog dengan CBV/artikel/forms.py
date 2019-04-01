from django.forms import ModelForm

from .models import Artikel


class ArtikelForm(ModelForm):
	class Meta:
		model = Artikel
		fields = [
			'judul',
			'isi',
			'kategori',
		]