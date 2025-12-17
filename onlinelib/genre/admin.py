from django.contrib import admin, messages

from .models import Genre, Tag, ContentWarning, AgeRating

# Register your models here.
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'level', 'status', 'parent')
    list_display_links = ('name', )
    # readonly_fields = ('slug',)
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 20
    search_fields = ('name',)
    list_editable = ('level', 'status', 'parent')
    list_filter = ('level', )
    actions = ('set_status_available', 'set_status_unavailable')

    @admin.action(description='Опубликовать')
    def set_status_available(self, request, queryset):
        count = queryset.update(status=Genre.StatusType.AVAILABLE)
        self.message_user(request, f'Изменено {count} записей!')

    @admin.action(description='Снять с публикации')
    def set_status_unavailable(self, request, queryset):
        count = queryset.update(status=Genre.StatusType.UNAVAILABLE)
        self.message_user(request, f'Изменено {count} записей!',
                          messages.WARNING)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_display_links = ('name', )
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)
    list_per_page = 20


@admin.register(ContentWarning)
class ContentWarningAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_display_links = ('name', )
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)
    list_per_page = 20


@admin.register(AgeRating)
class AgeRatingAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'min_age', 'max_age')
    list_display_links = ('name', )
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'min_age', 'max_age')
    list_editable = ('min_age', 'max_age')
    list_per_page = 20