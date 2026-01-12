from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView

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


class AddAuthor(FormView):
    form_class = AuthorForm
    template_name = 'author/add_author.html'
    success_url = reverse_lazy('author-home')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)