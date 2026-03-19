from django.utils.text import slugify

import factory
from factory.django import DjangoModelFactory

from ..models import Author
from users.tests.factories import UserFactory


class AuthorFactory(DjangoModelFactory):
    full_name = factory.Faker('name')
    slug = factory.LazyAttribute(lambda o: slugify(o.full_name))
    birth_date = factory.Faker('date_of_birth', minimum_age=18, maximum_age=80)
    bio = factory.Faker('text', max_nb_chars=200)
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = Author