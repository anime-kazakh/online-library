from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        unique=True,
    )
    description = models.TextField()