from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse_lazy

from genre.models import Genre, Tag, AgeRating, ContentWarning
from author.models import Author


class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Book.StatusType.AVAILABLE)


class Book(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    original_title = models.CharField(max_length=255, blank=True, null=True,
                                      verbose_name="Оригинальное название")
    slug = models.SlugField(max_length=255, unique=True, db_index=True,
                            verbose_name="slug")
    cover_image = models.ImageField(
        upload_to='books/covers/%Y/%m/%d/',
        blank=False, null=False,
        default='books/covers/default.png',
        verbose_name="Обложка"
    )
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    publication_year = models.IntegerField(blank=True, null=True, verbose_name="Год публикации")
    upload_date = models.DateField(auto_now_add=True, verbose_name="Дата загрузки")
    views_count = models.IntegerField(default=0, verbose_name="Количество просмотров")

    class StatusType(models.TextChoices):
        AVAILABLE = 'available', 'Активная'
        UNAVAILABLE = 'unavailable', 'Неактивная'

    status = models.CharField(max_length=255, choices=StatusType,
                              default=StatusType.AVAILABLE, verbose_name='Статус')
    authors = models.ManyToManyField(Author, verbose_name='Авторы',
                                     related_name='books', blank=True)
    genres = models.ManyToManyField(Genre, verbose_name='Жанры',
                                    related_name='books', blank=True)
    tags = models.ManyToManyField(Tag, verbose_name='Теги',
                                  related_name='books', blank=True)
    age_rating = models.ForeignKey(AgeRating, on_delete=models.SET_NULL, null=True, blank=True,
                                   verbose_name='Возрастной рейтинг', related_name='books')
    warnings = models.ManyToManyField(ContentWarning, verbose_name='Предупреждения',
                                      related_name='books', blank=True)
    post_author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL,
                                    related_name='books', verbose_name='Автор поста')

    objects = models.Manager()
    active = ActiveManager()

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('book-page', kwargs={ 'book_slug': self.slug })


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
                             verbose_name="Книга", related_name='files')
    book_file = models.FileField(
        upload_to='books/files/%Y/%m/%d/',
        default=None,
        blank=False,
        null=False,
        verbose_name="Файл"
    )
    language = models.ForeignKey(Language, on_delete=models.CASCADE,
                                 verbose_name="Язык")
    upload_date = models.DateField(auto_now_add=True, verbose_name="Дата загрузки")
    download_count = models.IntegerField(default=0, verbose_name="Количество скачиваний")
    post_author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL,
                                    related_name='files', verbose_name="Автор поста")

    class Meta:
        verbose_name = "Файл книги"
        verbose_name_plural = "Файлы книг"

    def __str__(self):
        return self.book_file.name

    def get_absolute_url(self):
        return self.book.get_absolute_url()