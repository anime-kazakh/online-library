import factory.fuzzy
from factory.django  import DjangoModelFactory

from ..models import BookScore, BookComments
from books.tests.factories import BookFactory
from users.tests.factories import UserFactory


class BookScoreFactory(DjangoModelFactory):
    book = factory.SubFactory(BookFactory)
    user = factory.SubFactory(UserFactory)
    score = factory.fuzzy.FuzzyInteger(1, 10)

    class Meta:
        model = BookScore


class BookCommentsFactory(DjangoModelFactory):
    book = factory.SubFactory(BookFactory)
    user = factory.SubFactory(UserFactory)
    comment = factory.Faker("text", max_nb_chars=200)
    
    class Meta:
        model = BookComments
