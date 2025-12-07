from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='author-home'),
    path('addauthor/', views.add_author, name='add-author'),
    path('<slug:author_slug>/', views.author_page, name='author-page'),
]