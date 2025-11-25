from django.db import models

# Create your models here.
class Author(models.Model):
    full_name = models.CharField(max_length=255)
    birth_date = models.DateField(blank=True, null=True)
    death_date = models.DateField(blank=True, null=True)
    photo = models.ImageField(
        upload_to='author/photos/%Y/%m/%d/',
        blank=False,
        null=False,
        default='author/photos/default.png'
    )
    bio = models.TextField(blank=True, null=True)