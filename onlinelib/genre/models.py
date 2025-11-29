from django.db import models
from django.urls import reverse


# Create your models here.
class Genre(models.Model):
    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        unique=True,
    )
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('genre-page', kwargs={ 'slug': self.slug })