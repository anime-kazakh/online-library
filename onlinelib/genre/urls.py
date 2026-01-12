from django.urls import path

from . import views


urlpatterns = [
    path('', views.GenreHome.as_view(), name='genre-home'),
    path('addgenre/', views.AddGenre.as_view(), name='add-genre'),
    path('addtag/', views.AddTag.as_view(), name='add-tag'),
    path('addcontentwarning/', views.AddContentWarning.as_view(), name='add-contentwarning'),
    path('addagerating/', views.AddAgeRating.as_view(), name='add-agerating'),
]