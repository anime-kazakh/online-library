from django import forms

from .models import Author


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('full_name', 'slug', 'birth_date', 'death_date', 'photo', 'bio')
        labels = {
            'slug': 'URL',
        }