import pytest

from ..serializers import AuthorSerializer


class TestAuthorSerializer:
    """
    Тестировнаие сериалайзеров
    """

    def test_set_user_default(self):
        AuthorSerializer()