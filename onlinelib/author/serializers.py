from rest_framework import serializers

from author.models import Author
from users.serializers import UserSerializer
from common.utils import AddCurrentUserMixin


class AuthorSerializer(AddCurrentUserMixin, serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Author
        fields = ('id', 'full_name', 'slug',
                  'birth_date', 'death_date', 'photo',
                  'bio', 'upload_date', 'user')
        read_only_fields = ('upload_date', 'user')
