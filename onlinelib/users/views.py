from django.contrib.auth.views import LoginView

from users.forms import LoginForm


class LoginUser(LoginView):
    form_class = LoginForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Вход'}

    # # По умолчанию редиректает в профиль users/profile
    # def get_success_url(self):
    #     return reverse_lazy('home')