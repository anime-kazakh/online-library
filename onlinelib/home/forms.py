from django import forms


class SearchForm(forms.Form):
    query = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'search-input'}))