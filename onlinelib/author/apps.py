from django.apps import AppConfig


class AuthorConfig(AppConfig):
    verbose_name = "Авторы"
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'author'
