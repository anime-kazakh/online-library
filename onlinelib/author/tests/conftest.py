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
def request_context(superuser):
    _request = APIRequestFactory()
    _request.user = superuser
    return _request