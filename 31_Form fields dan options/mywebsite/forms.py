from django import forms

class AllFormField(forms.Form):
	# Python data type
	integer_field		= forms.IntegerField()
	decimal_field 		= forms.DecimalField()
	float_filed 		= forms.FloatField()
	boolean_field		= forms.BooleanField()
	
	# String input
	char_field 			= forms.CharField()
	email_field 		= forms.EmailField()
	regex_field 		= forms.RegexField(regex=r'(P?<test>)')
	slug_field			= forms.SlugField()
	url_field			= forms.URLField()
	ip_field			= forms.GenericIPAddressField()
	
	# select
	PILIHAN = (
			('nilai 1','Pilihan 1'),
			('nilai 2','Pilihan 2'),
			('nilai 3','Pilihan 3'),
		)
	choice_field 		= forms.ChoiceField(choices=PILIHAN)
	multi_choice_field  = forms.MultipleChoiceField(choices=PILIHAN)
	multi_typed_choice  = forms.TypedMultipleChoiceField(choices=PILIHAN)
	null_boolean_field  = forms.NullBooleanField()

	# date time
	date_field 			= forms.DateField()
	datetime_field      = forms.DateTimeField()
	duration_field 		= forms.DurationField()
	time_field			= forms.TimeField()
	splitdatetime_field	= forms.SplitDateTimeField()

	# file input
	file_field 			= forms.FileField()
	image_field 		= forms.ImageField()