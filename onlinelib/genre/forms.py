from django import forms

from .models import Genre, Tag, ContentWarning, AgeRating


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ('name', 'slug', 'description', 'level', 'status', 'parent')
        labels = {
            'slug': 'URL',
        }


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('name', 'slug')
        labels = {
            'slug': 'Название в запросе',
        }


class ContentWarningForm(forms.ModelForm):
    class Meta:
        model = ContentWarning
        fields = ('name', 'slug')
        labels = {
            'slug': 'Название в запросе'
        }


class AgeRatingForm(forms.ModelForm):
    class Meta:
        model = AgeRating
        fields = ('name', 'slug', 'min_age', 'max_age')
        labels = {
            'slug': 'Название в запросе'
        }
