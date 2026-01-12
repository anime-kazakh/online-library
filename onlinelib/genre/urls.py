from django.urls import path

from . import views


urlpatterns = [
    path('', views.GenreHome.as_view(), name='genre-home'),
    path('addgenre/', views.AddGenre.as_view(), name='add-genre'),
    path('addtag/', views.AddTag.as_view(), name='add-tag'),
    path('addcontentwarning/', views.AddContentWarning.as_view(), name='add-contentwarning'),
    path('addagerating/', views.AddAgeRating.as_view(), name='add-agerating'),
    path('updategenre/<slug:slug>/', views.UpdateGenre.as_view(), name='update-genre'),
    path('updatetag/<slug:slug>/', views.UpdateTag.as_view(), name='update-tag'),
    path('updatecontentwarning/<slug:slug>/', views.UpdateContentWarning.as_view(), name='update-contentwarning'),
    path('updateagerating/<slug:slug>/', views.UpdateAgeRating.as_view(), name='update-agerating'),
    path('deletegenre/<slug:slug>/', views.DeleteGenre.as_view(), name='delete-genre'),
    path('deletetag/<slug:slug>/', views.DeleteTag.as_view(), name='delete-tag'),
    path('deletecontentwarning/<slug:slug>/', views.DeleteContentWarning.as_view(), name='delete-contentwarning'),
    path('deleteagerating/<slug:slug>/', views.DeleteAgeRating.as_view(), name='delete-agerating'),
    path('addagerating/', views.AddAgeRating.as_view(), name='add-agerating'),
]