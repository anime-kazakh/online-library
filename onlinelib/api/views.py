from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.exceptions import NotFound
from rest_framework import viewsets

from author.serializers import AuthorSerializer
from author.models import Author
from books.serializers import BookSerializer, FileSerializer, LanguageSerializer
from books.models import Book, Files, Language
from genre.serializers import GenreSerializer, TagSerializer, ContentWarningSerializer, AgeRatingSerializer
from genre.models import Genre, Tag, ContentWarning, AgeRating
from reactions.serializers import BookCommentsSerializer, BookScoreSerializer
from reactions.models import BookComments, BookScore


# ------------------Author API --------------------------------
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def perform_create(self, serializer):
        serializer.save(post_author=self.request.user)


# ------------------Books API --------------------------------
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        serializer.save(post_author=self.request.user)


class LanguageViewSets(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class FileViewSet(viewsets.ModelViewSet):
    queryset = Files.objects.all()
    serializer_class = FileSerializer

    def get_queryset(self):
        book_pk = self.kwargs.get('book_pk')
        book = get_object_or_404(Book, pk=book_pk)
        return Files.objects.filter(book=book)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset.exists():
            raise NotFound("Нет файлов.")
        return super().list(request, *args, **kwargs)

    def perform_create(self, serializer):
        book = get_object_or_404(Book, pk=self.kwargs.get('book_pk'))
        serializer.save(post_author=self.request.user, book=book)


# ------------------Genres API --------------------------------
class GenreViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class ContentWarningViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ContentWarning.objects.all()
    serializer_class = ContentWarningSerializer


class AgeRatingViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AgeRating.objects.all()
    serializer_class = AgeRatingSerializer


# ------------------Reactions API --------------------------------
class BookCommentViewSet(viewsets.ModelViewSet):
    serializer_class = BookCommentsSerializer
    queryset = BookComments.objects.all()

    def get_queryset(self):
        book_pk = self.kwargs.get('book_pk')
        book = get_object_or_404(Book, pk=book_pk)
        return BookComments.objects.filter(book=book)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset.exists():
            raise NotFound("Комментарии отсутствуют.")
        return super().list(request, *args, **kwargs)

    def perform_create(self, serializer):
        book = get_object_or_404(Book, pk=self.kwargs.get('book_pk'))
        serializer.save(user=self.request.user, book=book)


class BookScoreViewSet(viewsets.ModelViewSet):
    serializer_class = BookScoreSerializer
    queryset = BookScore.objects.all()

    def get_queryset(self):
        book_pk = self.kwargs.get('book_pk')
        book = get_object_or_404(Book, pk=book_pk)
        return BookScore.objects.filter(book=book)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset.exists():
            raise NotFound("Нет оценок.")
        return super().list(request, *args, **kwargs)

    def perform_create(self, serializer):
        book = get_object_or_404(Book, pk=self.kwargs.get('book_pk'))
        user = self.request.user

        if BookScore.objects.filter(book=book, user=user).exists():
            raise serializers.ValidationError('Вы уже оценили эту книгу')

        serializer.save(user=self.request.user, book=book)
