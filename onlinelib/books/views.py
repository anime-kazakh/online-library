from django.shortcuts import render

from .forms import BookForm, FileForm, LanguageForm
from .models import Book, Files

# Create your views here.
def index(request):
    data = {
        'books': Book.objects.filter(status='available')
    }
    return render(request, 'books/index.html', context=data)

def book_page(request, book_slug):
    book = Book.objects.get(slug=book_slug)
    data = {
        'book': book,
        'files': Files.objects.filter(book=book)
    }
    return render(request, 'books/book_page.html', context=data)

def add_book(request):
    data = {
        'form': BookForm(),
    }
    return render(request, 'books/add_record.html', context=data)

def add_file(request):
    data = {
        'form': FileForm(),
    }
    return render(request, 'books/add_record.html', context=data)

def add_language(request):
    data = {
        'form': LanguageForm(),
    }
    return render(request, 'books/add_record.html', context=data)