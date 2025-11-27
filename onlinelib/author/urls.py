from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='author-home'),
    path('/<slug:author_slug>/', views.author_page, name='author-page'),
]