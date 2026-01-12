from django.urls import path

from . import views


urlpatterns = [
    path('', views.BookHome.as_view(), name='books-home'),
    path('addbook/', views.AddBook.as_view(), name='add-book'),
    path('addfile/', views.AddFile.as_view(), name='add-file'),
    path('addlanguage/', views.AddLanguage.as_view(), name='add-language'),
    path('<slug:book_slug>/', views.BookPage.as_view(), name='book-page'),
]