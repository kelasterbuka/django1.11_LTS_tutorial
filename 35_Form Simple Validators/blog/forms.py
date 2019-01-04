from django import forms


class PostForm(forms.Form):
	judul		= forms.CharField(max_length = 20)
	body		= forms.CharField(
		widget = forms.Textarea
		)
	category	= forms.CharField(max_length = 20)

	def clean_judul(self):
		judul_input = self.cleaned_data.get('judul')

		if judul_input == "ucup":
			raise forms.ValidationError("ucup tidak boleh diposting")

		return judul_input