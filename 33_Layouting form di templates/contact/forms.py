# button
# text field
# text area
# password
# hidden field
# checkbox
# radio button
# radio group
# select

from django import forms

class ContactForm(forms.Form):
    nama_lengkap  = forms.CharField(
      label='Nama Lengkap',
      max_length=100,
      widget=forms.TextInput(
        attrs={
          'class':'form-control',
          'placeholder':'isi nama lengkap anda disini',}
          )
        )
    jenis_kelamin = forms.ChoiceField(
      label='Jenis kelamin',
      widget=forms.RadioSelect(),
      choices=[
          ('p','pria'),
          ('w','wanita')
          ]
        )
    TAHUN = range(1940,2020,1)
    tanggal_lahir = forms.DateField(
      widget=forms.SelectDateWidget(
        attrs={
          'class':'form-control col-sm-2',
        },
        years=TAHUN))
    email         = forms.EmailField(
      widget=forms.TextInput(
        attrs={
          'class':'form-control',
          'placeholder':'isi dengan email anda',
        }
      ),
      label="Alamat email")
    alamat        = forms.CharField(
      widget=forms.Textarea(
        attrs={
          'class':'form-control',
        }
      )
      )
    agree         = forms.BooleanField(label="semua data yang saya masukan adalah benar")
