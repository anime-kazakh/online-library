from django.db import models

from django.urls import reverse

# Create your models here.
class Author(models.Model):
    full_name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    birth_date = models.DateField(blank=True, null=True)
    death_date = models.DateField(blank=True, null=True)
    photo = models.ImageField(
        upload_to='author/photos/%Y/%m/%d/',
        blank=False,
        null=False,
        default='author/photos/default.png'
    )
    bio = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['full_name']

    def get_absolute_url(self):
        return reverse('author-page', kwargs={ 'slug': self.slug })