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
    jenis_kelamin = forms.ChoiceField(widget=forms.RadioSelect,
                                      choices=[
                                        ('p','pria'),
                                        ('w','wanita'),
                                        ])
    TAHUN = range(1940,2020,1)
    tanggal_lahir = forms.DateField(widget=forms.SelectDateWidget(years=TAHUN))
    email         = forms.EmailField(label="Alamat email")
    alamat        = forms.CharField(widget=forms.Textarea)
    agree         = forms.BooleanField()
