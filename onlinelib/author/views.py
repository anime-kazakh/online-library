from django.views.generic import ListView, DetailView, CreateView

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