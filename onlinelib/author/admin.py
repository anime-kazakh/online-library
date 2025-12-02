from django.contrib import admin
from .models import Author

# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'birth_date', 'death_date')
    list_display_links = ('id', 'full_name')
    ordering = [ 'full_name' ]
    list_per_page = 20