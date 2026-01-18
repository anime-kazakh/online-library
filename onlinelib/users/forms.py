from django import forms


class LoginForm(forms.Form):
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