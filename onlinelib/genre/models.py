from django.db import models
from mptt import models as mptt_models
from django.urls import reverse

# Create your models here.
class Genre(mptt_models.MPTTModel):
    name = models.CharField(max_length=255, blank=False, null=False,
                             unique=True, verbose_name="Жанр")
    slug = models.SlugField(max_length=255, unique=True, db_index=True,
                            verbose_name="slug")
    description = models.TextField(blank=True, null=True, verbose_name='Описание')

    class HierarchyType(models.TextChoices):
        ROOT = 'root', 'Корневой жанр'
        GROUP = 'group', 'Группа'
        GENERAL = 'general', 'Общий жанр'
        MAIN = 'main', 'Жанр'
        SUB = 'sub', 'Поджанр'

    hierarchy = models.CharField(max_length=255, choices=HierarchyType,
                             null=False, blank=False,
                             verbose_name="Уровень вложенности")

    class StatusType(models.TextChoices):
        AVAILABLE = 'available', 'Активная'
        UNAVAILABLE = 'unavailable', 'Неактивная'


    status = models.CharField(max_length=255, choices=StatusType,
                              default=StatusType.AVAILABLE, verbose_name="Статус")
    parent = mptt_models.TreeForeignKey('self', on_delete=models.CASCADE,
                                        null=True, blank=True,
                                        related_name='children', related_query_name='child',
                                        verbose_name='Родитель')

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


    class MPTTMeta:
        order_insertion_by = ('id', )


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('genre-page', kwargs={ 'genre_slug': self.slug })


class Tag(models.Model):
    name = models.CharField(max_length=255, blank=False,
                            null=False, verbose_name="Название")
    slug = models.SlugField(max_length=255, unique=True,
                            db_index=True, verbose_name="slug")

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"
        ordering = ['name']


    def __str__(self):
        return self.name


class ContentWarning(models.Model):
    name = models.CharField(max_length=255, blank=False,
                            null=False, verbose_name="Название")
    slug = models.SlugField(max_length=255, unique=True,
                            null=False, blank=False,
                            db_index=True, verbose_name="slug")

    class Meta:
        verbose_name = "Предупреждение о содержании"
        verbose_name_plural = "Предупреждения о содержании"
        ordering = ['name']


    def __str__(self):
        return self.name


class AgeRating(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False, verbose_name="Название")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="slug")
    min_age = models.PositiveSmallIntegerField(null=False, blank=False, verbose_name="Минимальный возраст")

    class Meta:
        verbose_name = "Возрастной рейтинг"
        verbose_name_plural = "Возрастные рейтинги"
        ordering = ['min_age']


    def __str__(self):
        return self.name