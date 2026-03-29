import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from django.utils import timezone

from books.serializers import (BookReadSerializer, BookWriteSerializer, AuthorSerializer,
                               FileReadSerializer, FileWriteSerializer, LanguageSerializer)


pytestmark = pytest.mark.django_db

class TestBookSerializer:
    """
    Тестирование сериализатора Book
    """
    def test_serializing(self, book):
        serializer = BookReadSerializer(instance=book)
        data = serializer.data

        assert data['id'] == book.id
        assert data['title'] == book.title
        assert data['original_title'] == book.original_title
        assert data['slug'] == book.slug
        assert data['description'] == book.description
        assert data['publication_year'] == int(book.publication_year)
        assert data['user']['id'] == book.user.id
        assert data['user']['username'] == book.user.username
        assert data['age_rating'] == book.age_rating.id

        for author in book.authors.all():
            author_data = AuthorSerializer(instance=author).data
            assert author_data in data['authors']

        for genre in book.genres.all():
            assert genre.id in data['genres']

        for tag in book.tags.all():
            assert tag.id in data['tags']

        for warning in book.warnings.all():
            assert warning.id in data['warnings']

        for file in book.files.all():
            file_data = FileReadSerializer(instance=file).data
            assert file_data in data['files']

    def test_deserializing(self, authors, genres, tags, age_rating, warnings, _request):
        data = {
            'title': 'test_title',
            'original_title': 'test_original_title',
            'slug': 'test_slug',
            'description': 'test_description',
            'publication_year': 2020,
            'authors': [a.id for a in authors],
            'genres': [g.id for g in genres[2: 4]],
            'tags': [t.id for t in tags],
            'age_rating': age_rating.id,
            'warnings': [w.id for w in warnings],
        }

        serializer = BookWriteSerializer(data=data, context={'request': _request})

        assert serializer.is_valid(), serializer.errors
        book = serializer.save()

        assert book.title == data['title']
        assert book.original_title == data['original_title']
        assert book.slug == data['slug']
        assert book.description == data['description']
        assert book.publication_year == data['publication_year']

        for b_author in book.authors.all():
            assert b_author in authors

        for b_genre in book.genres.all():
            assert b_genre in genres

        for b_tag in book.tags.all():
            assert b_tag in tags

        assert book.age_rating == age_rating

        for b_warning in book.warnings.all():
            assert b_warning in warnings

        assert book.user == _request.user


class TestFilesSerializer:
    """
    Тестирование класса Files
    """
    def test_serializing(self, file):
        serializer = FileReadSerializer(instance=file)
        data = serializer.data

        assert data['id'] == file.id
        assert data['book'] == file.book.id
        assert data['book_file'] == file.book_file.url
        assert data['language'] == LanguageSerializer(instance=file.language).data
        assert data['upload_date'] == file.upload_date.isoformat()
        assert data['download_count'] == file.download_count
        assert data['user']['id'] == file.user.id
        assert data['user']['username'] == file.user.username

    def test_deserializing(self, book, language, _request):
        file_content = b'test file text'
        up_file = SimpleUploadedFile(
            'test_file.txt',
            file_content,
            content_type='text/plain; charset=utf-8',
        )
        data = {
            'book': book.id,
            'book_file': up_file,
            'language': language.id,
        }

        serializer = FileWriteSerializer(data=data,
                                        context={'request': _request})
        assert serializer.is_valid(), serializer.errors
        file = serializer.save()

        assert file.book == book
        with file.book_file.open('rb') as f:
            text = f.read()
        assert file_content == text
        assert file.language == language
        assert file.upload_date == timezone.now().date()
        assert file.download_count == 0


class TestLanguagesSerializer:
    """
    Тестирование сериализатора Languages
    """
    def test_serializing(self, language):
        serializer = LanguageSerializer(instance=language)
        lang = serializer.data

        assert lang['id'] == language.id
        assert lang['name'] == language.name
        assert lang['code'] == language.code

    def test_deserializing(self):
        data = {
            'name': 'test_name',
            'code': 't_c',
        }
        serializer = LanguageSerializer(data=data)
        assert serializer.is_valid(), serializer.errors
        lang = serializer.save()
        assert lang.name == data['name']
        assert lang.code == data['code']

    def test_code_length(self):
        data = {
            'name': 'test_name',
            'code': '12345',
        }
        serializer = LanguageSerializer(data=data)

        assert not serializer.is_valid(), serializer.errors
