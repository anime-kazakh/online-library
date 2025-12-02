from django.contrib import admin, messages
from django.db.models.functions import Length
from .models import Book, Language, Files

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'original_title',
                    'slug', 'upload_date', 'views_count',
                    'status', 'description_info')
    list_display_links = ('id', 'title')
    readonly_fields = ('slug', 'views_count')
    ordering = ('title',)
    list_editable = ('status',)
    list_per_page = 20
    actions = ('set_status_available', 'set_status_unavailable')
    search_fields = ('title', 'original_title')
    list_filter = ('status', 'authors', 'genres')

    @admin.display(description="Длина описания (символы)", ordering=Length("description"))
    def description_info(self, book: Book):
        return len(book.description)

    @admin.action(description="Опубликовать записи")
    def set_status_available(self, request, queryset):
        count = queryset.update(status=Book.StatusType.AVAILABLE)
        self.message_user(request, f"Изменено {count} записей")

    @admin.action(description="Снять с публикации")
    def set_status_unavailable(self, request, queryset):
        count = queryset.update(status=Book.StatusType.UNAVAILABLE)
        self.message_user(request,f"Изменено {count} записей",
                          messages.WARNING)


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code')
    list_display_links = ('id', 'name', 'code')
    ordering = ('name',)
    list_per_page = 20
    search_fields = ('name', 'code')


@admin.register(Files)
class FilesAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'language', 'upload_date', 'download_count')
    list_display_links = ('id', 'book')
    readonly_fields = ('download_count',)
    list_per_page = 20
    search_fields = ('book__title', 'book__original_title')
    list_filter = ('language',)