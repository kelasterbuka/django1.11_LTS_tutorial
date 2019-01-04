from django.contrib import admin

# Register your models here.
from .models import PostModel

admin.site.register(PostModel)