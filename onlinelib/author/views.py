from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Author
from .forms import AuthorForm


class AuthorHome(ListView):
    model = Author
    template_name = 'author/index.html'
    context_object_name = 'authors'


class AuthorPage(DetailView):
    model = Author
    template_name = 'author/author_page.html'
    context_object_name = 'author'
    slug_url_kwarg = 'author_slug'


class AddAuthor(CreateView):
    form_class = AuthorForm
    template_name = 'author/add_author.html'


class UpdateAuthor(UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = 'author/add_author.html'


class DeleteAuthor(DeleteView):
    model = Author
    template_name = 'author/delete_confirm.html'
    success_url = reverse_lazy('author-home')