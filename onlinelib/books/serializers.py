from rest_framework import serializers

from .models import Book, Files, Language


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'


class FileSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    language = LanguageSerializer(read_only=True)

    class Meta:
        model = Files
        fields = '__all__'
        read_only_fields = ('upload_date', 'user')


class AuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    full_name = serializers.CharField()
    slug = serializers.CharField()


class BookSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    files = FileSerializer(many=True, read_only=True)
    authors = AuthorSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = '__all__'
        read_only_fields = ('upload_date', 'user')
