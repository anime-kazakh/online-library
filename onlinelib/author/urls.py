from django.urls import path

from . import views


urlpatterns = [
    path('', views.AuthorHome.as_view(), name='author-home'),
    path('addauthor/', views.add_author, name='add-author'),
    path('<slug:author_slug>/', views.AuthorPage.as_view(), name='author-page'),
]