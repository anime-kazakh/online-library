from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'class': 'form-field',
            'placeholder': 'Имя пользователя'
        })
    )
    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={
            'class': 'form-field',
            'placeholder': 'Пароль'
        })
    )

    class Meta:
        model = get_user_model()
        fields = ('username', 'password')