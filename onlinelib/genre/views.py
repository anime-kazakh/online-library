from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'genre/index.html')

def genre_page(request, genre_slug):
    return render(request, 'genre/index.html')