import pytest
from django.utils import timezone

from ..serializers import AuthorSerializer

pytestmark = pytest.mark.django_db

class TestAuthorSerializer:
    """
    Тестировнаие сериалайзеров
    """

    # --------------- serializing ---------------------------------
    def test_serializing(self, author):
        serializer = AuthorSerializer(instance=author)
        AuthorSerializer()
        data = serializer.data

        assert data['id'] == author.id
        assert data['full_name'] == author.full_name
        assert data['slug'] == author.slug
        assert data['birth_date'] == author.birth_date.isoformat()
        assert data['bio'] == author.bio
        assert data['user']['id'] == author.user.id
        assert data['user']['username'] == author.user.username

    # ------------- deserializing ----------------------------------
    def test_deserializing(self, user):
        data = {
            'full_name': 'test_name',
            'slug': 'test_slug',
            'birth_date': '1970-01-01',
            'bio': 'test_bio',
        }
        serializer = AuthorSerializer(data=data)
        assert serializer.is_valid(), serializer.errors
        author = serializer.save(user=user)
        assert author.full_name == data['full_name']
        assert author.slug == data['slug']
        assert author.birth_date.isoformat() == data['birth_date']
        assert author.bio == data['bio']
        assert author.user == user

    # --------------- read only fields ------------------------
    def test_read_only_fields(self, user):
        fake_upload_date = '2000-01-01'
        data = {
            'full_name': 'test_name',
            'slug': 'test_slug',
            'birth_date': '1970-01-01',
            'bio': 'test_bio',
            'upload_date': fake_upload_date,
            'user': user,
        }

        serializer = AuthorSerializer(data=data)
        assert serializer.is_valid(), serializer.errors
        author = serializer.save()

        assert author.upload_date != fake_upload_date
        assert author.upload_date == timezone.now().date()

        assert author.user != user

    # ---------------- validation ---------------------------
    def test_missing_required_fields(self):
        data = {}

        serializer = AuthorSerializer(data=data)
        assert not serializer.is_valid()
        assert 'full_name' in serializer.errors
        assert 'slug' in serializer.errors
