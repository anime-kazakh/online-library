from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Author

# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    fields = ('full_name', 'slug', 'birth_date', 'death_date',
              'photo', 'post_photo', 'bio', 'upload_date', 'post_author')
    list_display = ('id', 'full_name', 'post_photo', 'birth_date', 'death_date',
                    'upload_date', 'post_author__username')
    list_display_links = ('id', 'full_name')
    readonly_fields = ('post_photo',)
    prepopulated_fields = {'slug': ('full_name',)}
    ordering = ('full_name',)
    list_per_page = 20
    search_fields = ('full_name', 'post_author__username')
    list_filter = ('full_name', 'post_author__username')
    save_on_top = True

    @admin.display(description='Изображение автора')
    def post_photo(self, author: Author):
        return mark_safe(f'<img src="{author.photo.url}" width="50" height="50" />')
