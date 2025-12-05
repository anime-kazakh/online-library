from django.shortcuts import render

from .models import Genre

# Create your views here.
def index(request):
    data = {
        'genres': Genre.objects.all()
    }
    return render(request, 'genre/index.html', context=data)

def genre_page(request, genre_slug):
    return render(request, 'genre/index.html')