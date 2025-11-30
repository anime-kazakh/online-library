from django.contrib import admin
from .models import Book, Language, Files

# Register your models here.
admin.site.register([Book, Language, Files])