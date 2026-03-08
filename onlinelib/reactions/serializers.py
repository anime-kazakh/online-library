from rest_framework import serializers

from .models import BookComments, BookScore


class BookCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookComments
        fields = '__all__'
        read_only_fields = ('user', 'book', 'post_time', 'status')


class BookScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookScore
        fields = '__all__'
        read_only_fields = ('user', 'book')
