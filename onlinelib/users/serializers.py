from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        write_only=True,
        required=True,
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
        style={'input_type': 'password'},
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'},
    )

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'password',
                  'password2', 'email', 'first_name',
                  'last_name')
        read_only_fields = ('id', )
        extra_kwargs = {
            'first_name': {
                'required': False,
                'write_only': True,
            },
            'last_name': {
                'required': False,
                'write_only': True,
            },
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password': 'Пароли не совпадают'})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        return super().create(validated_data)