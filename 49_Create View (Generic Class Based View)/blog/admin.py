from django.contrib import admin

# Register your models here.
from .models import Artikel


class ArtikelAdmin(admin.ModelAdmin):
	readonly_fields = [
		'slug',
		'publish',
		'update',
	]

admin.site.register(Artikel,ArtikelAdmin)