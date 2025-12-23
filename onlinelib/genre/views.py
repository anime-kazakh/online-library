from django.shortcuts import render
from django.db.models import Q

from .models import Genre
from .forms import GenreForm

# Create your views here.
def index(request):
    data = {
        'genres': Genre.objects.filter(Q(hierarchy=Genre.HierarchyType.ROOT) |
                                       Q(hierarchy=Genre.HierarchyType.GROUP) |
                                       Q(hierarchy=Genre.HierarchyType.GENERAL))
    }
    return render(request, 'genre/index.html', context=data)

def genre_page(request, genre_slug):
    return render(request, 'genre/index.html')

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