from django.urls import path

from . import views


urlpatterns = [
    path('', views.AuthorHome.as_view(), name='author-home'),
    path('addauthor/', views.AddAuthor.as_view(), name='add-author'),
    path('updateauthor/<slug:slug>/', views.UpdateAuthor.as_view(), name='update-author'),
    path('deleteauthor/<slug:slug>/', views.DeleteAuthor.as_view(), name='delete-author'),
    path('<slug:author_slug>/', views.AuthorPage.as_view(), name='author-page'),
]