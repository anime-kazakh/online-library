from django.shortcuts import render
from django.views.generic import ListView

from genre.models import Genre
from .forms import BookForm, FileForm, LanguageForm
from .models import Book, Files
from .filters import BookFilter


class BookHome(ListView):
    model = Book
    queryset = Book.active.all()
    # Default <app-name>/<model-name>_list.html
    template_name = 'books/index.html'
    # Default object_list
    context_object_name = 'books'
    # For some extra context
    extra_context = {
        'genres': Genre.objects.all()
    }

    def get_queryset(self):
        queryset = super().get_queryset()

        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        flt = context['filter'] = BookFilter(self.request.GET,
                                       queryset=context['books'])

        return context


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