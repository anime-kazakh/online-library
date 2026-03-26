import pytest
from django.utils import timezone

from ..serializers import AuthorSerializer
from users.tests.factories import UserFactory


pytestmark = pytest.mark.django_db

class TestAuthorSerializer:
    """
    Тестировнаие сериалайзеров
    """

    # --------------- serializing ---------------------------------
    def test_serializing(self, author):
        serializer = AuthorSerializer(instance=author)
        data = serializer.data

        assert data['id'] == author.id
        assert data['full_name'] == author.full_name
        assert data['slug'] == author.slug
        assert data['birth_date'] == author.birth_date.isoformat()
        assert data['bio'] == author.bio
        assert data['user']['id'] == author.user.id
        assert data['user']['username'] == author.user.username

    # ------------- deserializing ----------------------------------
    def test_deserializing(self, request_context):
        data = {
            'full_name': 'test_name',
            'slug': 'test_slug',
            'birth_date': '1970-01-01',
            'bio': 'test_bio',
        }

        serializer = AuthorSerializer(data=data, context={'request': request_context})
        assert serializer.is_valid(), serializer.errors
        author = serializer.save()
        assert author.full_name == data['full_name']
        assert author.slug == data['slug']
        assert author.birth_date.isoformat() == data['birth_date']
        assert author.bio == data['bio']
        assert author.user.id == request_context.user.id
        assert author.user.username == request_context.user.username

    # --------------- read only fields ------------------------
    def test_read_only_fields(self, request_context):
        fake_upload_date = '2000-01-01'
        data = {
            'full_name': 'test_name',
            'slug': 'test_slug',
            'birth_date': '1970-01-01',
            'bio': 'test_bio',
            'upload_date': fake_upload_date,
            'user': UserFactory(),
        }

        serializer = AuthorSerializer(data=data, context={'request': request_context})
        assert serializer.is_valid(), serializer.errors
        author = serializer.save()

        assert author.upload_date != fake_upload_date
        assert author.upload_date == timezone.now().date()

        assert author.user != data['user']

    # ---------------- validation ---------------------------
    def test_missing_required_fields(self):
        data = {}

        serializer = AuthorSerializer(data=data)
        assert not serializer.is_valid()
        assert 'full_name' in serializer.errors
        assert 'slug' in serializer.errors
