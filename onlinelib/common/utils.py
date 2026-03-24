from django.core.exceptions import PermissionDenied

menu = [
    { 'title': 'Жанры', 'url_name': 'genre-home' },
    { 'title': 'Авторы', 'url_name': 'author-home' },
    { 'title': 'Книги', 'url_name': 'books-home' },
    { 'title': 'О сайте', 'url_name': 'about' },
]

class DataMixin:
    title_page = None
    extra_context = {}

    def __init__(self):
        if self.title_page:
            self.extra_context['title'] = self.title_page

        if 'menu' not in self.extra_context:
            self.extra_context['menu'] = menu

    # def get_mixin_context(self, context, **kwargs):
    #     context['menu'] = self.extra_context['menu']
    #     context.update(kwargs)
    #     return context


class PermissionMixin:
    """
    Проверяет, является ли автором статьи или суперпользователем.
    ! Модель должна содержать поле user.
    """
    def get_object(self, queryset=None):
        model = super().get_object(queryset)
        if self.request.user.is_superuser: return model
        if self.request.user != model.user:
            raise PermissionDenied
        return model


class AddCurrentUserMixin:
    """
    Добавляет в поле user текущего пользователя из контекста.
    ! Модель и сериализатор должны содержать поле user.
    """

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)