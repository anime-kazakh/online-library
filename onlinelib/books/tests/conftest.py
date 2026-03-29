import pytest
from rest_framework.test import APIRequestFactory, force_authenticate

from .factories import BookFactory, LanguageFactory, FilesFactory
from users.tests.factories import UserFactory
from author.tests.factories import AuthorFactory
from genre.tests.factories import (GenreFactory, TagFactory, AgeRatingFactory,
                                   ContentWarningFactory, GenreTreeFactory)


@pytest.fixture
def language():
    return LanguageFactory()

@pytest.fixture
def file(language):
    return FilesFactory(language=language)

@pytest.fixture
def authors():
    return [AuthorFactory(),
            AuthorFactory()]

@pytest.fixture
def genres():
    return GenreTreeFactory.create_tree()

@pytest.fixture
def tags():
    return [TagFactory(),
            TagFactory()]

@pytest.fixture
def warnings():
    return [ContentWarningFactory(),
            ContentWarningFactory()]

@pytest.fixture
def age_rating():
    return AgeRatingFactory()

@pytest.fixture
def book():
    return BookFactory(
        authors=[AuthorFactory()],
        genres=[GenreFactory(), GenreFactory()],
        tags=[TagFactory(), TagFactory()],
        age_rating=AgeRatingFactory(),
        warnings=[ContentWarningFactory()]
    )

@pytest.fixture
def superuser():
    return UserFactory(admin=True)

@pytest.fixture
def _request(superuser):
    req = APIRequestFactory()
    req.user = superuser
    return req