from django.shortcuts import render
from django.views.generic import ListView, DetailView

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


def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else: form = AuthorForm()

    data = {
        'form': form,
    }
    return render(request, 'author/add_author.html', context=data)