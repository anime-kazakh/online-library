from django import forms

from .models import Book, Files, Language
from author.models import Author
from genre.models import Genre, Tag, ContentWarning, AgeRating


class BookForm(forms.ModelForm):
    authors = forms.ModelMultipleChoiceField(queryset=Author.objects.all(), label='Авторы')
    genres = forms.ModelMultipleChoiceField(queryset=Genre.objects.all(), label='Жанры')
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), label='Теги')
    warnings = forms.ModelMultipleChoiceField(queryset=ContentWarning.objects.all(),
                                              label='Предупреждения о содержании')
    class Meta:
        model = Book
        fields = ('title', 'original_title', 'slug',
                  'cover_image', 'description', 'publication_year',
                  'status', 'authors', 'genres', 'tags',
                  'age_rating', 'warnings')
        # widgets = {
        #     'isbn': forms.Textarea(attrs={'rows': 2, 'cols': 40}),
        # }
        labels = {
            'slug': 'URL'
        }


class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ('name', 'code')


class FileForm(forms.ModelForm):
    class Meta:
        model = Files
        fields = ('book', 'book_file', 'language')