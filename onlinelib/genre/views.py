from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Genre, Tag, ContentWarning, AgeRating
from .forms import GenreForm, TagForm, ContentWarningForm, AgeRatingForm


class GenreHome(ListView):
    model = Genre
    template_name = 'genre/index.html'
    context_object_name = 'genres'
    queryset = Genre.main_level.all()


class AddGenre(CreateView):
    form_class = GenreForm
    template_name = 'genre/add_record.html'
    success_url = reverse_lazy('genre-home')


class UpdateGenre(UpdateView):
    model = Genre
    form_class = GenreForm
    template_name = 'genre/add_record.html'
    success_url = reverse_lazy('genre-home')


class DeleteGenre(DeleteView):
    model = Genre
    template_name = 'genre/delete_confirm.html'
    success_url = reverse_lazy('genre-home')


class AddTag(CreateView):
    form_class = TagForm
    template_name = 'genre/add_record.html'
    success_url = reverse_lazy('genre-home')


class UpdateTag(UpdateView):
    model = Tag
    form_class = TagForm
    template_name = 'genre/add_record.html'
    success_url = reverse_lazy('genre-home')


class DeleteTag(DeleteView):
    model = Tag
    template_name = 'genre/delete_confirm.html'
    success_url = reverse_lazy('genre-home')


class AddContentWarning(CreateView):
    form_class = ContentWarningForm
    template_name = 'genre/add_record.html'
    success_url = reverse_lazy('genre-home')


class UpdateContentWarning(UpdateView):
    model = ContentWarning
    form_class = ContentWarningForm
    template_name = 'genre/add_record.html'
    success_url = reverse_lazy('genre-home')


class DeleteContentWarning(DeleteView):
    model = ContentWarning
    template_name = 'genre/delete_confirm.html'
    success_url = reverse_lazy('genre-home')


class AddAgeRating(CreateView):
    form_class = AgeRatingForm
    template_name = 'genre/add_record.html'
    success_url = reverse_lazy('genre-home')


class UpdateAgeRating(UpdateView):
    model = AgeRating
    form_class = AgeRatingForm
    template_name = 'genre/add_record.html'
    success_url = reverse_lazy('genre-home')


class DeleteAgeRating(DeleteView):
    model = AgeRating
    template_name = 'genre/delete_confirm.html'
    success_url = reverse_lazy('genre-home')