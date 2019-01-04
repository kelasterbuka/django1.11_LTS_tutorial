from django import forms


class PostForm(forms.Form):
	judul		= forms.CharField(max_length = 20)
	body		= forms.CharField(
		widget = forms.Textarea
		)
	category	= forms.CharField(max_length = 20)