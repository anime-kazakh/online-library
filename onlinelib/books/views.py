from django.shortcuts import render

from .models import Book, Files

# Create your views here.
def index(request):
    data = {
        'books': Book.objects.filter(status='available')
    }
    return render(request, 'index.html', context=data)

def book_page(request, book_slug):
    book = Book.objects.get(slug=book_slug)
    data = {
        'book': book,
        'files': Files.objects.filter(book=book)
    }
    return render(request, 'book_page.html', context=data)