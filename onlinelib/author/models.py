from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

# from transliterate import slugify

# Create your models here.
class Author(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="ФИО")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="slug")
    birth_date = models.DateField(blank=True, null=True, verbose_name="Дата рождения")
    death_date = models.DateField(blank=True, null=True, verbose_name="Дата смерти")
    photo = models.ImageField(
        upload_to='author/photos/%Y/%m/%d/',
        blank=False,
        null=False,
        default='author/photos/default.png',
        verbose_name="Фотография"
    )
    bio = models.TextField(blank=True, null=True, verbose_name="Биография")
    upload_date = models.DateField(auto_now_add=True, verbose_name="Время публикации")
    post_author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True,
                                    related_name="authors", verbose_name="Автор поста",)

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"
        ordering = ['full_name']

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return reverse('author-page', kwargs={ 'author_slug': self.slug })

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.full_name)
    #     super().save(*args, **kwargs)