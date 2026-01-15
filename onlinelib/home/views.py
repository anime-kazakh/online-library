from random import randint

from django.db.models import Q
from django.views.generic import TemplateView

from .forms import SearchForm
from .utils import DataMixin

from author.models import Author
from books.models import Book
from genre.models import Genre


class Home(DataMixin, TemplateView):
    template_name = 'home/index.html'
    title_page = 'ONLINELIB'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books_mostpop'] = Book.objects.order_by('views_count')[:5]
        rand_pk = randint(1, Book.objects.count())
        context['rand_book'] = Book.objects.get(pk=rand_pk)
        return context


class About(DataMixin, TemplateView):
    template_name = 'home/about.html'
    title_page = 'О сайте'


class Search(DataMixin, TemplateView):
    template_name = 'home/search.html'
    title_page = 'Поиск'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'query' in self.request.GET:
            form = SearchForm(self.request.GET)
            if form.is_valid():
                query = form.cleaned_data['query']

                context['authors'] = Author.objects.filter(full_name__icontains=query)
                context['books'] = Book.objects.filter(Q(title__icontains=query) |
                                                       Q(original_title__icontains=query))
                context['genres'] = Genre.objects.filter(name__icontains=query)
        else: form = SearchForm()
        context['form'] = form

        return context