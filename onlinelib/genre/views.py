from django.urls import reverse_lazy
from django.views.generic import ListView, FormView

from .models import Genre
from .forms import GenreForm, TagForm, ContentWarningForm, AgeRatingForm


class GenreHome(ListView):
    model = Genre
    template_name = 'genre/index.html'
    context_object_name = 'genres'
    queryset = Genre.main_level.all()


class AddGenre(FormView):
    form_class = GenreForm
    template_name = 'genre/add_record.html'
    success_url = reverse_lazy('genre-home')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class AddTag(FormView):
    form_class = TagForm
    template_name = 'genre/add_record.html'
    success_url = reverse_lazy('genre-home')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class AddContentWarning(FormView):
    form_class = ContentWarningForm
    template_name = 'genre/add_record.html'
    success_url = reverse_lazy('genre-home')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class AddAgeRating(FormView):
    form_class = AgeRatingForm
    template_name = 'genre/add_record.html'
    success_url = reverse_lazy('genre-home')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)