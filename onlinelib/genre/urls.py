from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='genre-home'),
    path('<slug:genre_slug>/', views.genre_page, name='genre-page'),
]