from django.urls import path

from . import views


urlpatterns = [
    path('', views.GenreHome.as_view(), name='genre-home'),
    path('addgenre/', views.add_genre, name='add-genre'),
]