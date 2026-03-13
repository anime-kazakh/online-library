from rest_framework import serializers

from author.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Author
        fields = '__all__'
        read_only_fields = ('upload_date', 'post_author')