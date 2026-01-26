from django.urls import path
from . import views


app_name = 'reactions'

urlpatterns = [
    path('add-book-comment/', views.add_book_comment, name='add-book-comment'),
    path('delete-book-comment/', views.delete_book_comment, name='delete-book-comment'),
    path('book-rate/', views.book_rate, name='book-rate'),
]