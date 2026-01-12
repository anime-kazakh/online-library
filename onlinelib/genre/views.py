from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .models import Genre
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


class AddTag(CreateView):
    form_class = TagForm
    template_name = 'genre/add_record.html'
    success_url = reverse_lazy('genre-home')


class AddContentWarning(CreateView):
    form_class = ContentWarningForm
    template_name = 'genre/add_record.html'
    success_url = reverse_lazy('genre-home')


class AddAgeRating(CreateView):
    form_class = AgeRatingForm
    template_name = 'genre/add_record.html'
    success_url = reverse_lazy('genre-home')