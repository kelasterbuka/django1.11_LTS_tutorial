from django.core.exceptions import ValidationError

def validate_author(value):
	judul_input = value
	if judul_input == "Einstein":
		message = "maaf, " + judul_input + " tidak bisa posting"
		raise ValidationError(message)