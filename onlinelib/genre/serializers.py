from rest_framework import serializers

from .models import Genre, Tag, ContentWarning, AgeRating


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ContentWarningSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentWarning
        fields = '__all__'


class AgeRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgeRating
        fields = '__all__'
