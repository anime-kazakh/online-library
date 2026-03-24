import pytest
from django.db import IntegrityError
from django.urls import reverse

from .factories import BookFactory, LanguageFactory, FilesFactory
from ..models import Book, DEFAULT_COVER_IMAGE, Language, Files

pytestmark = pytest.mark.django_db

class TestBooksModel:
    """
    Тестирование модели книг
    """

    # ---------------- Creation -----------------------------
    def test_create_book(self, book):
        assert Book.objects.filter(slug=book.slug).exists()

    # ---------------- __str__ ------------------------------
    def test_str(self, book):
        assert str(book) == book.title

    # ---------------- slug unique --------------------------
    def test_slug_unique(self):
        BookFactory(slug='test-slug')
        with pytest.raises(IntegrityError):
            BookFactory(slug='test-slug')

    # --------------------- default ------------------------
    def test_cover_image_default(self, book):
        assert book.cover_image is not None
        assert str(book.cover_image) == DEFAULT_COVER_IMAGE

    def test_upload_date_auto_now(self, book):
        assert book.upload_date is not None
        from datetime import date
        assert book.upload_date <= date.today()

    def test_views_count_is_zero(self, book):
        assert book.views_count == 0

    def test_status_default(self, book):
        assert book.status == Book.StatusType.AVAILABLE

    # ---------------- url ----------------------------------
    def test_get_absolute_url(self, book):
        expected_url = reverse('book-page', kwargs={'book_slug': book.slug})
        assert book.get_absolute_url() == expected_url

class TestLanguageModel:
    """
    Тестирование модели Language
    """
    def test_language_creation(self, language):
        lang = Language.objects.filter(name=language.code)
        assert lang.exists()
        assert lang.first().name == language.name
        assert lang.first().code == language.code

    def test_unique_code(self):
        LanguageFactory(code='T-C')

        with pytest.raises(IntegrityError):
            LanguageFactory(code='T-C')

    def test_str(self, language):
        assert str(language) == (language.name + ' - ' + language.code)

    def test_null_name(self):
        with pytest.raises(IntegrityError):
            LanguageFactory(name=None)

    def test_null_code(self):
        with pytest.raises(IntegrityError):
            LanguageFactory(code=None)


class TestFilesModel:
    """
    Тестирование модели Files
    """

    def test_file_creation(self, file):
        _file = Files.objects.filter(id=file.id)
        assert _file.exists()
        assert _file.first().book_file == file.book_file
        assert _file.first().book == file.book

    def test_get_absolute_url(self):
        book = BookFactory()
        file = FilesFactory(book=book)

        assert file.get_absolute_url() == book.get_absolute_url()

    def test_str(self, file):
        assert str(file) == (file.book_file.name)

