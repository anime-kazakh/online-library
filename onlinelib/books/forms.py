from django import forms

from .models import Book, Files, Language


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'original_title', 'slug',
                  'cover_image', 'description', 'publication_year',
                  'isbn', 'status', 'authors', 'genres')


class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ('name', 'code')


class FileForm(forms.ModelForm):
    class Meta:
        model = Files
        fields = ('book', 'book_file', 'language')