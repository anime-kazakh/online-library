from django.core.cache import cache

from celery import shared_task

from .models import Book


@shared_task
def update_books_views_count(slug):
    """
    Обновление БД(book.views_count)
    """

    cache_key = f"books:{slug}:views_count"
    current_views = cache.get(cache_key)

    Book.objects.filter(slug=slug).update(views_count=current_views)
