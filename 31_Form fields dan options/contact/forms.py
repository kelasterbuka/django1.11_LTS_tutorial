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
    nama_lengkap  = forms.CharField(max_length=100)
    jenis_kelamin = forms.ChoiceField(choices=[
                                        ('p','pria'),
                                        ('w','wanita'),
                                        ])
    email         = forms.EmailField(label="Alamat email")
    alamat        = forms.CharField(required=False)
    kode_pos      = forms.DecimalField(required=False)
    kota          = forms.CharField(required=False)
    provinsi      = forms.CharField(required=False)
    agree         = forms.BooleanField()
