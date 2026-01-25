from django.urls import path
from . import views


app_name = 'reactions'

urlpatterns = [
    path('add-book-comment/', views.add_book_comment, name='add-book-comment'),
]