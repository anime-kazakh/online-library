from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView

from .models import Genre
from .forms import GenreForm


class GenreHome(ListView):
    model = Genre
    template_name = 'genre/index.html'
    context_object_name = 'genres'
    queryset = Genre.main_level.all()


def genre_page(request, genre_slug):
    return redirect(reverse('books-home', query={'genres': genre_slug}))

def add_genre(request):
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = GenreForm()

    data = {
        'form': form,
    }
    return render(request, 'genre/add_genre.html', context=data)