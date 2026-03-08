from django.urls import path, include

from rest_framework import routers

from . import views
from .views import AuthorViewSet

app_name = 'api'

router = routers.SimpleRouter()
router.register(r'authors', AuthorViewSet)

urlpatterns = [
    # ------------------------Author API Path-----------------------------------
    # path('authors/', views.AuthorListAPIView.as_view(), name='author-list'),
    # path('authors/<int:pk>/', views.AuthorDetailAPIView.as_view(), name='author-detail'),
    path('', include(router.urls)),
    # -------------------Books & Reactions API Path------------------------------
    path('books/', views.BookListAPIView.as_view(), name='book-list'),
    path('books/<int:book>/', views.BookDetailAPIView.as_view(), name='book-detail'),
    path('books/<int:book>/comments/', views.BookCommentListAPIView.as_view(), name='book-comments'),
    path('books/<int:book>/scores/', views.BookScoreListAPIView.as_view(), name='book-scores'),
    path('books/comments/destroy/<int:comment>/', views.BookCommentDestroyAPIView.as_view(), name='book-comment-destroy'),
    path('languages/', views.LanguageListAPIView.as_view(), name='language-list'),
    path('languages/<int:pk>/', views.LanguageDetailAPIView.as_view(), name='language-detail'),
    path('files/', views.FileListAPIView.as_view(), name='file-list'),
    path('files/<int:book>/', views.FileDetailAPIView.as_view(), name='file-detail'),
    # ------------------------Genres API Path-----------------------------------
    path('genres/', views.GenreListAPIView.as_view(), name='genre-list'),
    path('tags/', views.TagListAPIView.as_view(), name='tag-list'),
    path('contentwarnings/', views.ContentWarningListAPIView.as_view(), name='content-warning-list'),
    path('ageratings/', views.AgeRatingListAPIView.as_view(), name='agerating-list'),
]