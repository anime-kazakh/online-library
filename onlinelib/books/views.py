from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

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

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     queryset.prefetch_related('files')
    #     return queryset

    def get_object(self, queryset=None):
        return get_object_or_404(Book.active, slug=self.kwargs[self.slug_url_kwarg])


class AddBook(CreateView):
    form_class = BookForm
    template_name = 'books/add_record.html'


class AddFile(CreateView):
    form_class = FileForm
    template_name = 'books/add_record.html'


class AddLanguage(CreateView):
    form_class = LanguageForm
    template_name = 'books/add_record.html'
    success_url = reverse_lazy('books-home')