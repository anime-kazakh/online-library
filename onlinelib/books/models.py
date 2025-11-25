from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    original_title = models.CharField(max_length=255, blank=True, null=True)
    cover_image = models.ImageField(
        upload_to='books/covers/%Y/%m/%d/',
        blank=False,
        null=False,
        default='books/covers/default.png',
    )
    description = models.TextField(blank=True, null=True)
    publication_year = models.IntegerField(blank=True, null=True)
    isbn = models.TextField(blank=True, null=True)
    upload_date = models.DateField(auto_now_add=True)
    views_count = models.IntegerField(default=0)
    status_type = models.TextChoices('status_type', 'available unavailable')
    status = models.TextField(choices=status_type, default='available')


class Language(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    code = models.CharField(max_length=3, null=False, blank=False, unique=True)


class Files(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    book_file = models.FileField(
        upload_to='books/files/%Y/%m/%d/',
        default=None,
        blank=False,
        null=False,
    )
    file_size = models.IntegerField(default=0)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    upload_date = models.DateField(auto_now_add=True, blank=False, null=False)
    download_count = models.IntegerField(default=0)

