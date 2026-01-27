from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import ValidationError


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'class': 'form-field',
            'placeholder': 'Имя пользователя / E-Mail'
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


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'class': 'form-field',
            'placeholder': 'Имя пользователя'
        })
    )
    password1 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={
            'class': 'form-field',
            'placeholder': 'Пароль'
        })
    )
    password2 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={
            'class': 'form-field',
            'placeholder': 'Повтор пароля'
        })
    )

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
        labels = {
            'email': '',
            'first_name': '',
            'last_name': '',
        }
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-field'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Имя','class': 'form-field'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Фамилия', 'class': 'form-field'}),
        }

    # def clean_password2(self):
    #     cd = self.cleaned_data
    #     if cd['password'] != cd['password2']:
    #         raise ValidationError("Пароли не совпадают")
    #     return cd['password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise ValidationError('Такой email существует')
        return email


class ProfileUserForm(forms.ModelForm):
    username = forms.CharField(disabled=True, label='Имя пользователя',
                               widget=forms.TextInput(attrs={'class': 'form-field'}))
    email = forms.EmailField(disabled=True, label='E-mail',
                             widget=forms.EmailInput(attrs={'class': 'form-field'}))

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name')
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-field'}),
            'last_name': forms.TextInput(attrs={'class': 'form-field'}),
        }