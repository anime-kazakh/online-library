from django.utils.text import slugify

import factory
from factory.django import DjangoModelFactory

from ..models import Book, Files, Language
from author.tests.factories import AuthorFactory
from users.tests.factories import UserFactory


class BookFactory(DjangoModelFactory):
    class Meta:
        model = Book

    title = factory.Faker('sentence', nb_words=4)
    original_title = factory.Faker('sentence', nb_words=4)
    slug = factory.LazyAttribute(lambda o: slugify(o.title))
    description = factory.Faker('paragraph', nb_sentences=3)
    publication_year = factory.Faker('year')
    authors = factory.SubFactory(AuthorFactory)
    user = factory.SubFactory(UserFactory)

    @factory.post_generation
    def authors(self, create, extracted, **kwargs):
        if not create or not extracted:
            return None

        return self.authors.add(*extracted)

    @factory.post_generation
    def genres(self, create, extracted, **kwargs):
        if not create or not extracted:
            return None

        return self.genres.add(*extracted)

    @factory.post_generation
    def tags(self, create, extracted, **kwargs):
        if not create or not extracted:
            return None

        return self.tags.add(*extracted)

    @factory.post_generation
    def warnings(self, create, extracted, **kwargs):
        if not create or not extracted:
            return None

        return self.warnings.add(*extracted)


class LanguageFactory(DjangoModelFactory):
    class Meta:
        model = Language

    name = factory.Sequence(lambda n: f'L{n}')
    code = factory.LazyAttribute(lambda o: f'{o.name}')


class FilesFactory(DjangoModelFactory):
    class Meta:
        model = Files

    book = factory.SubFactory(BookFactory)
    book_file = factory.django.FileField(
        filename='test_file.txt',
        content_type = 'Text',
        data = b'Test file data',
    )
    language = factory.SubFactory(LanguageFactory)
    user = factory.SubFactory(UserFactory)