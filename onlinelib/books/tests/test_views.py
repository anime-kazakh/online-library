import pytest
from django.urls import reverse

from .factories import BookFactory


pytestmark = pytest.mark.django_db

class TestBookView:
    """
    Тестирование Book Views
    """

    # -------------- book-home -------------------
    def test_book_home(self, client):
        books = BookFactory.create_batch(5)

        url = reverse('books-home')
        response = client.get(url)

        assert response.status_code == 200
        assert 'books/index.html' in response.template_name

        for _book in books:
            assert _book.title in response.content.decode()

    # -------------- book-page -------------------
    def test_book_page(self, client, mocker):
        book = BookFactory.create()
        url = reverse('book-page', kwargs={'book_slug': book.slug})

        mocker.patch('books.views.cache')
        mocker.patch('books.views.update_books_views_count')

        response = client.get(url)

        assert response.status_code == 200
        assert 'books/book_page.html' in response.template_name

        page = response.content.decode()
        assert book.title in page
        assert book.original_title in page

        for author in book.authors.all():
            assert author.full_name in page

        for genre in book.genres.all():
            assert genre.name in page

        for tag in book.tags.all():
            assert tag.name in page

        assert f'{book.age_rating.min_age}+' in page

    def test_view_count_incr(self, client, mocker):
        book = BookFactory.create()
        url = reverse('book-page', kwargs={'book_slug': book.slug})

        mock_cache = mocker.patch('books.views.cache')
        mock_cache.incr.return_value = 10
        cel_task = mocker.patch('books.views.update_books_views_count')

        response = client.get(url)

        assert response.status_code == 200

        cel_task.assert_called_once_with(book.slug)
