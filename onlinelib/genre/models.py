from django.db import models
from django.urls import reverse

# from transliterate import slugify

# Create your models here.
class Genre(models.Model):
    name = models.CharField( max_length=255, blank=False, null=False,
                             unique=True, verbose_name="Жанр")
    slug = models.SlugField(max_length=255, unique=True, db_index=True,
                            verbose_name="slug")
    description = models.TextField(blank=True, null=True,
                                   verbose_name="Описание")

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('genre-page', kwargs={ 'genre_slug': self.slug })

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.name)
    #     super().save(*args, **kwargs)