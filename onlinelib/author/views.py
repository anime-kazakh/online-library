from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from common.utils import DataMixin, PermissionMixin
from .models import Author
from .forms import AuthorForm


class AuthorHome(DataMixin, ListView):
    model = Author
    template_name = 'author/index.html'
    context_object_name = 'authors'
    title_page = 'Авторы'
    paginate_by = 5


class AuthorPage(DataMixin, DetailView):
    model = Author
    template_name = 'author/author_page.html'
    context_object_name = 'author'
    slug_url_kwarg = 'author_slug'


class AddAuthor(PermissionRequiredMixin, LoginRequiredMixin, DataMixin, CreateView):
    form_class = AuthorForm
    template_name = 'author/add_author.html'
    title_page = 'Добавление автора'
    # login_url = 'users:login'
    permission_required = 'author.add_author'  # <app>.<action>_<tab>

    def form_valid(self, form):
        w = form.save(commit=False)
        w.post_author = self.request.user
        return super().form_valid(form)


class UpdateAuthor(PermissionRequiredMixin, LoginRequiredMixin, PermissionMixin, DataMixin, UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = 'author/add_author.html'
    title_page = 'Редактирование автора'
    permission_required = 'author.change_author'


class DeleteAuthor(PermissionRequiredMixin, LoginRequiredMixin, PermissionMixin, DataMixin, DeleteView):
    model = Author
    template_name = 'author/delete_confirm.html'
    success_url = reverse_lazy('author-home')
    title_page = 'Удаление автора'
    permission_required = 'author.delete_author'
