from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from home.utils import DataMixin
from .models import Author
from .forms import AuthorForm


class AuthorHome(DataMixin, ListView):
    model = Author
    template_name = 'author/index.html'
    context_object_name = 'authors'
    title_page = 'Авторы'


class AuthorPage(DataMixin, DetailView):
    model = Author
    template_name = 'author/author_page.html'
    context_object_name = 'author'
    slug_url_kwarg = 'author_slug'


class AddAuthor(DataMixin, CreateView):
    form_class = AuthorForm
    template_name = 'author/add_author.html'
    title_page = 'Добавление автора'


class UpdateAuthor(DataMixin, UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = 'author/add_author.html'
    title_page = 'Редактирование автора'


class DeleteAuthor(DataMixin, DeleteView):
    model = Author
    template_name = 'author/delete_confirm.html'
    success_url = reverse_lazy('author-home')
    title_page = 'Удаление автора'