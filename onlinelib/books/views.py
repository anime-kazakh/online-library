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
    book.views_count = book.views_count + 1
    book.save()
    data = {
        'book': book,
        'files': Files.objects.filter(book=book)
    }
    return render(request, 'books/book_page.html', context=data)

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = BookForm()
    data = {
        'form': form,
    }
    return render(request, 'books/add_record.html', context=data)

def add_file(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = FileForm()
    data = {
        'form': form,
    }
    return render(request, 'books/add_record.html', context=data)

def add_language(request):
    if request.method == 'POST':
        form = LanguageForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = LanguageForm()
    data = {
        'form': form,
    }
    return render(request, 'books/add_record.html', context=data)