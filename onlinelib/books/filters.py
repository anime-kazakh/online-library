from django import forms

from author.models import Author
from .models import Book
from genre.models import Genre, Tag, AgeRating, ContentWarning

import django_filters
from django_filters import widgets


class BookFilter(django_filters.FilterSet):
    genres = django_filters.ModelMultipleChoiceFilter(
        field_name='genres__slug',
        to_field_name='slug',
        queryset=Genre.objects.all(),
        label='Жанры',
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'genre-check'}),
    )
    tags = django_filters.ModelMultipleChoiceFilter(
        field_name='tags__slug',
        to_field_name='slug',
        queryset=Tag.objects.all(),
        label='Теги',
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'tag-check'}),
    )
    authors = django_filters.ModelMultipleChoiceFilter(
        field_name='authors__slug',
        to_field_name='slug',
        queryset=Author.objects.all(),
        label='Авторы',
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'author-check'}),
    )
    age_rating = django_filters.ModelMultipleChoiceFilter(
        field_name='age_rating__slug',
        to_field_name='slug',
        queryset=AgeRating.objects.all(),
        label='Возрастной рейтинг',
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'age-check'}),
    )
    warnings = django_filters.ModelMultipleChoiceFilter(
        field_name='warnings__slug',
        to_field_name='slug',
        queryset=ContentWarning.objects.all(),
        label='Предупреждения',
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'warning-check'}),
    )
    publication_year = django_filters.RangeFilter(
        label='Год выпуска',
        required=False,
        initial={ 'min': None, 'max': None },
        widget=widgets.RangeWidget(attrs={
            'class': 'publication-year',
            'placeholder': 'YYYY'
        })
    )

    class Meta:
        model = Book
        fields = ('genres', 'tags', 'authors',
                  'age_rating', 'warnings',
                  'publication_year')