from django.contrib import admin, messages

from .models import BookComments, BookScore


@admin.register(BookScore)
class BookScoreAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'score')
    list_display_links = ('book', 'user')
    list_per_page = 20
    list_editable = ('score',)
    search_fields = ('book__title', 'user__username')



@admin.register(BookComments)
class BookCommentsAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'status', 'post_time', 'comment_count')
    list_display_links = ('book', 'user')
    readonly_fields = ('post_time', )
    list_per_page = 20
    list_editable = ('status', )
    search_fields = ('book__title', 'user__username')
    list_filter = ('status', 'book', 'user')
    save_on_top = True

    # @admin.display(description='Название книги')
    # def book_title(self, comment: BookComments):
    #     return comment.book.title
    #
    # @admin.display(description='Имя пользователя')
    # def user_name(self, comment: BookComments):
    #     return comment.user.username

    @admin.display(description='Длинна комментария')
    def comment_count(self, comment: BookComments):
        return len(comment.comment)

    @admin.action(description="Опубликовать записи")
    def set_status_available(self, request, queryset):
        count = queryset.update(status=BookComments.StatusType.AVAILABLE)
        self.message_user(request, f"Изменено {count} записей")

    @admin.action(description="Поставить на модерацию")
    def set_status_moderation(self, request, queryset):
        count = queryset.update(status=BookComments.StatusType.MODERATION)
        self.message_user(request, f"Изменено {count} записей")

    @admin.action(description="Снять с публикации")
    def set_status_unavailable(self, request, queryset):
        count = queryset.update(status=BookComments.StatusType.UNAVAILABLE)
        self.message_user(request, f"Изменено {count} записей",
                          messages.WARNING)