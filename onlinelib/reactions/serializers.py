from rest_framework import serializers

from .models import BookComments, BookScore


class BookCommentsSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = BookComments
        fields = '__all__'
        read_only_fields = ('book', 'post_time', 'status')


class BookScoreSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = BookScore
        fields = '__all__'
        read_only_fields = ('book', )
