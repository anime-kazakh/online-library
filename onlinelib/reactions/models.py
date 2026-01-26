from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from books.models import Book


class ExistingManager(models.Manager):
    def get_or_none(self, **kwargs):
        try:
            return self.get(**kwargs)
        except self.model.DoesNotExist:
            return None


class BookScore(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE,
                             related_name='score', verbose_name="Книга")
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                             related_name='score', verbose_name="Пользователь")
    score = models.IntegerField(validators=[MinValueValidator(1),
                                            MaxValueValidator(10)],
                                verbose_name="Оценка")

    objects = models.Manager()
    existing = ExistingManager()

    class Meta:
        verbose_name = "Книжная оценка"
        verbose_name_plural = "Книжные оценки"
        unique_together = ('book', 'user')


class BookComments(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE,
                             related_name='comments', verbose_name="Книга")
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                             related_name='comments', verbose_name="Пользователь")
    comment = models.TextField(max_length=1000, verbose_name="Комментарий")
    post_time = models.DateTimeField(auto_now_add=True, verbose_name="Время публикации")

    class StatusType(models.TextChoices):
        AVAILABLE = 'available', 'Активная'
        MODERATION = 'moderation', 'На модерации'
        UNAVAILABLE = 'unavailable', 'Неактивная'

    status = models.CharField(max_length=20, choices=StatusType,
                              default=StatusType.AVAILABLE, verbose_name='Статус')

    class Meta:
        verbose_name = "Книжный комментарий"
        verbose_name_plural = "Книжные комментарии"
        ordering = ['-id',]