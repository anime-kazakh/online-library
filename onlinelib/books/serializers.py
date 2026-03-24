from rest_framework import serializers

from .models import Book, Files, Language
from users.serializers import UserSerializer
from common.utils import AddCurrentUserMixin


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'


class FileSerializer(AddCurrentUserMixin, serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    language = LanguageSerializer(read_only=True)

    class Meta:
        model = Files
        fields = '__all__'
        read_only_fields = ('upload_date', 'user')


class AuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    full_name = serializers.CharField()
    slug = serializers.CharField()


class BookSerializer(AddCurrentUserMixin, serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    files = FileSerializer(many=True, read_only=True)
    authors = AuthorSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = '__all__'
        read_only_fields = ('upload_date', 'user')
