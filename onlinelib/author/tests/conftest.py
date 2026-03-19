import pytest

from .factories import AuthorFactory


@pytest.fixture
def author():
    return AuthorFactory()