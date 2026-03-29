from rest_framework import serializers

from .models import Book, Files, Language
from users.serializers import UserSerializer
from common.utils import AddCurrentUserMixin


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('id', 'name', 'code')


class FileReadSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    language = LanguageSerializer(read_only=True)

    class Meta:
        model = Files
        fields = ('id', 'book', 'book_file',
                  'language', 'upload_date',
                  'download_count', 'user')
        read_only_fields = ('upload_date', 'download_count', 'user')


class FileWriteSerializer(AddCurrentUserMixin, serializers.ModelSerializer):
    class Meta:
        model = Files
        fields = ('id', 'book', 'book_file',
                  'language', 'upload_date',
                  'download_count', 'user')
        read_only_fields = ('upload_date', 'download_count', 'user')


class AuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    full_name = serializers.CharField()
    slug = serializers.CharField()


class BookReadSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    files = FileReadSerializer(many=True, read_only=True)
    authors = AuthorSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ('id', 'title', 'original_title',
                  'slug', 'cover_image', 'description',
                  'publication_year', 'upload_date',
                  'views_count', 'status', 'authors',
                  'genres', 'tags', 'age_rating',
                  'warnings', 'files', 'user')
        read_only_fields = ('upload_date', 'user')


class BookWriteSerializer(AddCurrentUserMixin, serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'original_title',
                  'slug', 'cover_image', 'description',
                  'publication_year', 'upload_date',
                  'views_count', 'status', 'authors',
                  'genres', 'tags', 'age_rating',
                  'warnings', 'user')
        read_only_fields = ('upload_date', 'user')