from django.db import models
from django.urls import reverse

# from transliterate import slugify

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    original_title = models.CharField(max_length=255, blank=True, null=True,
                                      verbose_name="Оригинальное название")
    slug = models.SlugField(max_length=255, unique=True, db_index=True,
                            verbose_name="slug")
    cover_image = models.ImageField(
        upload_to='books/covers/%Y/%m/%d/',
        blank=False,
        null=False,
        default='books/covers/default.png',
        verbose_name="Обложка"
    )
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    publication_year = models.IntegerField(blank=True, null=True, verbose_name="Год публикации")
    isbn = models.TextField(blank=True, null=True, verbose_name="isbn")
    upload_date = models.DateField(auto_now_add=True, verbose_name="Дата загрузки")
    views_count = models.IntegerField(default=0, verbose_name="Количество просмотров")

    class StatusType(models.TextChoices):
        AVAILABLE = 'available', 'Активная'
        UNAVAILABLE = 'unavailable', 'Неактиваня'


    status = models.TextField(choices=StatusType, default=StatusType.AVAILABLE,
                              verbose_name="Статус")
    authors = models.ManyToManyField('author.Author', blank=True,
                                     related_name='books', verbose_name="Авторы")
    genres = models.ManyToManyField('genre.Genre', blank=True,
                                    related_name='books', verbose_name="Жанры")

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-page', kwargs={ 'book_slug': self.slug })

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)


class Language(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False,
                            verbose_name="Язык")
    code = models.CharField(max_length=3, null=False, blank=False,
                            unique=True, verbose_name="Код")

    class Meta:
        verbose_name = "Язык"
        verbose_name_plural = "Языки"

    def __str__(self):
        return self.name + ' - ' + self.code


class Files(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE,
                             verbose_name="Книга")
    book_file = models.FileField(
        upload_to='books/files/%Y/%m/%d/',
        default=None,
        blank=False,
        null=False,
        verbose_name="Файл"
    )
    language = models.ForeignKey(Language, on_delete=models.CASCADE,
                                 verbose_name="Язык")
    upload_date = models.DateField(auto_now_add=True, blank=False,
                                   null=False, verbose_name="Дата загрузки")
    download_count = models.IntegerField(default=0,
                                         verbose_name="Количество скачиваний")

    class Meta:
        verbose_name = "Файл книги"
        verbose_name_plural = "Файлы книг"

    def __str__(self):
        return self.book_file.name