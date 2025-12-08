from django.shortcuts import render

from .models import Genre
from .forms import GenreForm

# Create your views here.
def index(request):
    data = {
        'genres': Genre.objects.all()
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