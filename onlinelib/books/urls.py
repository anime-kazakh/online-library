from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='books-home'),
    path('<slug:book_slug>/', views.book_page, name='book-page'),
]