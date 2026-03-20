import pytest
from django.contrib.auth.models import Group, Permission

from users.tests.factories import UserFactory
from .factories import AuthorFactory


@pytest.fixture
def author():
    return AuthorFactory()

@pytest.fixture
def superuser():
    return UserFactory(admin=True)