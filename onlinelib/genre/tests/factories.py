from django.utils.text import slugify
import factory
from factory.django import DjangoModelFactory

from ..models import Genre, Tag, AgeRating, ContentWarning


class GenreFactory(DjangoModelFactory):
    """
    Файбрика модели жанров.
    """
    class Meta:
        model = Genre

    name = factory.Sequence(lambda n: f'Genre{n}')
    slug = factory.LazyAttribute(lambda o: slugify(o.name))
    description = factory.Faker('sentence', nb_words=10)
    hierarchy = Genre.HierarchyType.ROOT
    parent = None


class GenreTreeFactory(DjangoModelFactory):
    """
    Генериция дерева.
    """

    @staticmethod
    def _hierarchy_map(hierarchy:int=0)->Genre.HierarchyType:
        match hierarchy:
            case 0:
                return Genre.HierarchyType.ROOT
            case 1:
                return Genre.HierarchyType.GROUP
            case 2:
                return Genre.HierarchyType.GENERAL
            case 3:
                return Genre.HierarchyType.MAIN
            case _:
                return Genre.HierarchyType.SUB

    @staticmethod
    def create_tree(depth=2, children_per_node=3,
                    hierarchy=0, parent=None):
        """
        Рекурсивное создание дерева.

        ! hierarchy:
            0 - ROOT
            1 - GROUP
            2 - GENERAL
            3 - MAIN
            4 - SUB
        """
        genres = []
        for i in range(children_per_node):
            genre = GenreFactory.create(
                parent=parent,
                hierarchy=GenreTreeFactory._hierarchy_map(hierarchy)
            )
            genres.append(genre)

            if depth > 1:
                sub_gen = GenreTreeFactory.create_tree(
                    depth=depth - 1,
                    children_per_node=children_per_node,
                    parent=genre,
                    hierarchy=hierarchy + 1
                )
                genres.extend(sub_gen)

        return genres


class TagFactory(DjangoModelFactory):
    class Meta:
        model = Tag

    name = factory.Sequence(lambda n: f'Tag{n}')
    slug = factory.LazyAttribute(lambda o: slugify(o.name))


class ContentWarningFactory(DjangoModelFactory):
    class Meta:
        model = ContentWarning

    name = factory.Sequence(lambda n: f'ContentWarning{n}')
    slug = factory.LazyAttribute(lambda o: slugify(o.name))


class AgeRatingFactory(DjangoModelFactory):
    class Meta:
        model = AgeRating

    name = factory.Sequence(lambda n: f'AgeRating{n}')
    slug = factory.LazyAttribute(lambda o: slugify(o.name))
    min_age = factory.Sequence(lambda n: n)
