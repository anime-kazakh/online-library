from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.exceptions import NotFound
from rest_framework import generics, viewsets

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

# ------------------Books API --------------------------------
class BookListAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # lookup_field = 'slug'
    lookup_url_kwarg = 'book'


class LanguageListAPIView(generics.ListCreateAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class LanguageDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class FileListAPIView(generics.ListCreateAPIView):
    queryset = Files.objects.all()
    serializer_class = FileSerializer


class FileDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Files.objects.all()
    serializer_class = FileSerializer
    lookup_field = 'book'
    lookup_url_kwarg = 'book'


# ------------------Genres API --------------------------------
class GenreListAPIView(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class TagListAPIView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class ContentWarningListAPIView(generics.ListAPIView):
    queryset = ContentWarning.objects.all()
    serializer_class = ContentWarningSerializer


class AgeRatingListAPIView(generics.ListAPIView):
    queryset = AgeRating.objects.all()
    serializer_class = AgeRatingSerializer


# ------------------Reactions API --------------------------------
class BookCommentListAPIView(generics.ListCreateAPIView):
    serializer_class = BookCommentsSerializer
    lookup_field = 'book'
    lookup_url_kwarg = 'book'

    def get_queryset(self):
        book_pk = self.kwargs.get(self.lookup_url_kwarg)
        book = get_object_or_404(Book, pk=book_pk)
        return BookComments.objects.filter(book=book)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset.exists():
            raise NotFound("Комментарии отсутствуют.")
        return super().list(request, *args, **kwargs)

    def perform_create(self, serializer):
        book = get_object_or_404(Book, pk=self.kwargs.get(self.lookup_url_kwarg))
        serializer.save(user=self.request.user, book=book)


class BookCommentDestroyAPIView(generics.DestroyAPIView):
    queryset = BookComments.objects.all()
    serializer_class = BookCommentsSerializer
    lookup_url_kwarg = 'comment'


class BookScoreListAPIView(generics.ListCreateAPIView):
    serializer_class = BookScoreSerializer
    lookup_field = 'book'
    lookup_url_kwarg = 'book'

    def get_queryset(self):
        book_pk = self.kwargs.get(self.lookup_url_kwarg)
        book = get_object_or_404(Book, pk=book_pk)
        return BookScore.objects.filter(book=book)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset.exists():
            raise NotFound("Нет оценок.")
        return super().list(request, *args, **kwargs)

    def perform_create(self, serializer):
        book = get_object_or_404(Book, pk=self.kwargs.get(self.lookup_url_kwarg))
        user = self.request.user

        if BookScore.objects.filter(book=book, user=user).exists():
            raise serializers.ValidationError('Вы уже оценили эту книгу')

        serializer.save(user=self.request.user, book=book)
