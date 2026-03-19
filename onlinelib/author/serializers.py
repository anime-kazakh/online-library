from rest_framework import serializers

from author.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    # user = serializers.ReadOnlyField(default=serializers.CurrentUserDefault())
    user = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Author
        fields = ('id', 'full_name', 'slug',
                  'birth_date', 'death_date', 'photo',
                  'bio', 'upload_date', 'user')
        read_only_fields = ('upload_date', 'user')

    def get_user(self, obj):
        return {
            'id': obj.user.id,
            'username': obj.user.username,
        }