import pytest
from django.db import IntegrityError
from django.urls import reverse

from ..models import Author, DEFAULT_AUTHOR_PHOTO
from .factories import AuthorFactory

pytestmark = pytest.mark.django_db

class TestAuthorModel:
    """
    Тестирование модели Author
    """

    # ------------ Создание -----------------------
    def test_create_author(self):
        author = AuthorFactory()

        assert Author.objects.filter(
            full_name=author.full_name,
            slug=author.slug,
        ).exists()

    # ------------- __str__ -----------------------
    def test_str(self):
        author = AuthorFactory()
        assert str(author) == author.full_name

    # ------------ get_absolute_url ---------------
    def test_get_absolute_url(self):
        author = AuthorFactory()
        url = author.get_absolute_url()
        expected = reverse('author-page',
                           kwargs={'author_slug': author.slug})
        assert url == expected

    # ------------ slug unique --------------------
    def test_slug_unique(self):
        AuthorFactory(slug='test-slug')
        with pytest.raises(IntegrityError):
            AuthorFactory(slug='test-slug')

    # ------------ default photo ------------------
    def test_photo_default(self):
        author = AuthorFactory()

        assert author.photo is not None
        assert str(author.photo) == DEFAULT_AUTHOR_PHOTO