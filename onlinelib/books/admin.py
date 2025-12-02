from django.contrib import admin
from .models import Book, Language, Files

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'original_title',
                    'slug', 'upload_date', 'views_count',
                    'status')
    list_display_links = ('id', 'title')
    ordering = ['title']
    list_editable = [ 'status' ]
    list_per_page = 20


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code')
    list_display_links = ('id', 'name', 'code')
    ordering = ['name']
    list_per_page = 20


@admin.register(Files)
class FilesAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'language', 'upload_date', 'download_count')
    list_display_links = ('id', 'book')
    list_per_page = 20