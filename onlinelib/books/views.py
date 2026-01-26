from django.db.models import Avg
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.db.models import F
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from common.utils import DataMixin
from genre.models import Genre
from .forms import BookForm, FileForm, LanguageForm
from .models import Book, Files, Language
from .filters import BookFilter
from reactions.froms import CommentForm


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
    extra_context = {
        'comment_form': CommentForm()
    }

    def get_object(self, queryset=None):
        return get_object_or_404(Book.active, slug=self.kwargs[self.slug_url_kwarg])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = context['book']
        avg_score = book.score.aggregate(Avg('score'))['score__avg']
        context['avg_score'] = round(avg_score, 1) if avg_score else 0
        if self.request.user.is_authenticated:
            user_score = book.score.get(user=self.request.user)
            if user_score:
                context['user_score'] = user_score.score
        return context

def file_download(request, file_id):
    file = get_object_or_404(Files, pk=file_id)

    Files.objects.filter(pk=file_id).update(download_count=F('download_count') + 1)

    return FileResponse(file.book_file.open('rb'), as_attachment=True)


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

    def get_initial(self):
        initial = super().get_initial()
        book_id = self.request.GET.get('book')
        if book_id:
            initial['book'] = book_id
        return initial


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


# Пользователь не должен иметь возможность удалять языки
# этим будет заниматься суперпользователь
# class AddLanguage(DataMixin, CreateView):
#     form_class = LanguageForm
#     template_name = 'books/add_record.html'
#     success_url = reverse_lazy('books-home')
#     title_page = 'Добавление языка'
#
#
# class UpdateLanguage(DataMixin, UpdateView):
#     model = Language
#     fields = ('name', 'code')
#     template_name = 'books/add_record.html'
#     success_url = reverse_lazy('books-home')
#     title_page = 'Редактирование языка'
#
#
# class DeleteLanguage(DataMixin, DeleteView):
#     model = Language
#     template_name = 'books/delete_confirm.html'
#     success_url = reverse_lazy('books-home')
#     title_page = 'Удаление языка'