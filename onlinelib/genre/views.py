from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from home.utils import DataMixin
from .models import Genre, Tag, ContentWarning, AgeRating
from .forms import GenreForm, TagForm, ContentWarningForm, AgeRatingForm


class GenreHome(DataMixin, ListView):
    model = Genre
    template_name = 'genre/index.html'
    context_object_name = 'genres'
    queryset = Genre.main_level.all()
    title_page = 'Жанры'


class AddGenre(DataMixin, CreateView):
    form_class = GenreForm
    template_name = 'genre/add_record.html'
    success_url = reverse_lazy('genre-home')
    title_page = 'Добавление Жанра'


class UpdateGenre(DataMixin, UpdateView):
    model = Genre
    form_class = GenreForm
    template_name = 'genre/add_record.html'
    success_url = reverse_lazy('genre-home')
    title_page = 'Редактирование Жанра'


class DeleteGenre(DataMixin, DeleteView):
    model = Genre
    template_name = 'genre/delete_confirm.html'
    success_url = reverse_lazy('genre-home')
    title_page = 'Удаление Жанра'


class AddTag(DataMixin, CreateView):
    form_class = TagForm
    template_name = 'genre/add_record.html'
    success_url = reverse_lazy('genre-home')
    title_page = 'Добавление Тега'


class UpdateTag(DataMixin, UpdateView):
    model = Tag
    form_class = TagForm
    template_name = 'genre/add_record.html'
    success_url = reverse_lazy('genre-home')
    title_page = 'Редактирование Тега'


class DeleteTag(DataMixin, DeleteView):
    model = Tag
    template_name = 'genre/delete_confirm.html'
    success_url = reverse_lazy('genre-home')
    title_page = 'Удаление Тега'


class AddContentWarning(DataMixin, CreateView):
    form_class = ContentWarningForm
    template_name = 'genre/add_record.html'
    success_url = reverse_lazy('genre-home')
    title_page = 'Добавление Предупреждения'


class UpdateContentWarning(DataMixin, UpdateView):
    model = ContentWarning
    form_class = ContentWarningForm
    template_name = 'genre/add_record.html'
    success_url = reverse_lazy('genre-home')
    title_page = 'Редактирование Предупреждения'


class DeleteContentWarning(DataMixin, DeleteView):
    model = ContentWarning
    template_name = 'genre/delete_confirm.html'
    success_url = reverse_lazy('genre-home')
    title_page = 'Удаление Предупреждения'


class AddAgeRating(DataMixin, CreateView):
    form_class = AgeRatingForm
    template_name = 'genre/add_record.html'
    success_url = reverse_lazy('genre-home')
    title_page = 'Добавление Возрастного рейтинга'


class UpdateAgeRating(DataMixin, UpdateView):
    model = AgeRating
    form_class = AgeRatingForm
    template_name = 'genre/add_record.html'
    success_url = reverse_lazy('genre-home')
    title_page = 'Редактирование Возрастного рейтинга'


class DeleteAgeRating(DataMixin, DeleteView):
    model = AgeRating
    template_name = 'genre/delete_confirm.html'
    success_url = reverse_lazy('genre-home')
    title_page = 'Удаление Возрастного рейтинга'