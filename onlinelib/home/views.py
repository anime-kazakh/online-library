from django.shortcuts import render
from django.db.models import Q

from .forms import SearchForm

from author.models import Author
from books.models import Book
from genre.models import Genre

def index(request):
    data = {  }
    return render(request, 'home/index.html', context=data)

def about(request):
    data = {}
    return render(request, 'home/about.html', context=data)

def search(request):
    data = {}
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']

            data['authors'] = Author.objects.filter(full_name__icontains=query)
            data['books'] = Book.objects.filter(Q(title__icontains=query) |
                                                Q(original_title__icontains=query))
            data['genres'] = Genre.objects.filter(name__icontains=query)
    else:
        form = SearchForm()

    data['form'] = form

    return render(request, 'home/search.html', context=data)