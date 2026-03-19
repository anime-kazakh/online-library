import pytest

from rest_framework.test import APIClient

from users.tests.factories import UserFactory


@pytest.fixture
def api_ref():
    return APIClient()

@pytest.fixture
def user():
    return UserFactory()