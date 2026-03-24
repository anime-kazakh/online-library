import pytest

from .factories import BookFactory, LanguageFactory, FilesFactory


@pytest.fixture
def book():
    return BookFactory()

@pytest.fixture
def language():
    return LanguageFactory()

@pytest.fixture
def file():
    return FilesFactory()