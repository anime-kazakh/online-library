from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from genre.models import Genre
from .forms import BookForm, FileForm, LanguageForm
from .models import Book
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

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['filter'] = BookFilter(self.request.GET,
                                       queryset=context['books'])
        return context


class BookPage(DetailView):
    model = Book
    template_name = 'books/book_page.html'
    slug_url_kwarg = 'book_slug'
    context_object_name = 'book'

    def get_object(self, queryset=None):
        return get_object_or_404(Book.active, slug=self.kwargs[self.slug_url_kwarg])


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