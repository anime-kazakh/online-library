import pytest
from rest_framework.test import APIRequestFactory

from users.tests.factories import UserFactory
from .factories import AuthorFactory


@pytest.fixture
def author():
    return AuthorFactory()

@pytest.fixture
def superuser():
    return UserFactory(admin=True)

@pytest.fixture
def _request(superuser):
    _req = APIRequestFactory()
    _req.user = superuser
    return _req