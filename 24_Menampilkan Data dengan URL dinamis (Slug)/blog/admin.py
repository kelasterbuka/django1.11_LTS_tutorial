from django.contrib import admin
from django.utils.html import format_html_join

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):	
	readonly_fields = ['slug',]

admin.site.register(Post, PostAdmin)