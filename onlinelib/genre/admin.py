from django.contrib import admin
from .models import Genre

# Register your models here.
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name')
    readonly_fields = ('slug',)
    list_per_page = 20
    search_fields = ('name',)