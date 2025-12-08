from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='books-home'),
    path('addbook/', views.add_book, name='add-book'),
    path('addfile/', views.add_file, name='add-file'),
    path('addlanguage/', views.add_language, name='add-language'),
    path('<slug:book_slug>/', views.book_page, name='book-page'),
]