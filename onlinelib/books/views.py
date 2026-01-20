from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from common.utils import DataMixin
from genre.models import Genre
from .forms import BookForm, FileForm, LanguageForm
from .models import Book, Files, Language
from .filters import BookFilter


class BookHome(DataMixin, ListView):
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
    title_page = "Книги"
    paginate_by = 20 # Слайсает и невозможно пользоваться фильтром

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['filter'] = BookFilter(self.request.GET,
                                       queryset=self.get_queryset())
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return BookFilter(self.request.GET, queryset=queryset).qs


class BookPage(DataMixin, DetailView):
    model = Book
    template_name = 'books/book_page.html'
    slug_url_kwarg = 'book_slug'
    context_object_name = 'book'

    def get_object(self, queryset=None):
        return get_object_or_404(Book.active, slug=self.kwargs[self.slug_url_kwarg])


class AddBook(DataMixin, CreateView):
    form_class = BookForm
    # We can create CreateView without form
    # model = Book
    # fields = '__all__'
    # fields = ('name', 'slug', ...)
    template_name = 'books/add_record.html'
    title_page = 'Добавление книги'


class UpdateBook(DataMixin, UpdateView):
    model = Book
    fields = ('title', 'original_title', 'cover_image', 'description',
              'publication_year', 'status', 'authors', 'genres',
              'tags', 'age_rating', 'warnings')
    template_name = 'books/add_record.html'
    title_page = 'Редактирование книги'


class DeleteBook(DataMixin, DeleteView):
    model = Book
    template_name = 'books/delete_confirm.html'
    success_url = reverse_lazy('books-home')
    title_page = 'Удаление книги'


class AddFile(DataMixin, CreateView):
    form_class = FileForm
    template_name = 'books/add_record.html'
    title_page = 'Добавление файла'


class UpdateFile(DataMixin, UpdateView):
    model = Files
    fields = ('book', 'book_file', 'language')
    template_name = 'books/add_record.html'
    title_page = 'Редактирование файла'


class DeleteFile(DataMixin, DeleteView):
    model = Files
    template_name = 'books/delete_confirm.html'
    success_url = reverse_lazy('books-home')
    title_page = 'Удаление файла'


class AddLanguage(DataMixin, CreateView):
    form_class = LanguageForm
    template_name = 'books/add_record.html'
    success_url = reverse_lazy('books-home')
    title_page = 'Добавление языка'


class UpdateLanguage(DataMixin, UpdateView):
    model = Language
    fields = ('name', 'code')
    template_name = 'books/add_record.html'
    success_url = reverse_lazy('books-home')
    title_page = 'Редактирование языка'


class DeleteLanguage(DataMixin, DeleteView):
    model = Language
    template_name = 'books/delete_confirm.html'
    success_url = reverse_lazy('books-home')
    title_page = 'Удаление языка'