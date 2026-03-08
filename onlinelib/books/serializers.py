from rest_framework import serializers

from .models import Book, Files, Language


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Files
        fields = '__all__'
