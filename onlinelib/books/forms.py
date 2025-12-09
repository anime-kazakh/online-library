from django import forms

from .models import Book, Files, Language
from author.models import Author
from genre.models import Genre


class BookForm(forms.ModelForm):
    authors = forms.ModelMultipleChoiceField(queryset=Author.objects.all(), label='Авторы')
    genres = forms.ModelMultipleChoiceField(queryset=Genre.objects.all(), label='Жанры')
    class Meta:
        model = Book
        fields = ('title', 'original_title', 'slug',
                  'cover_image', 'description', 'publication_year',
                  'isbn', 'status', 'authors', 'genres')
        widgets = {
            'isbn': forms.Textarea(attrs={'rows': 2, 'cols': 40}),
        }
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