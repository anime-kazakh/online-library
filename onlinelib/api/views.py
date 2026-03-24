from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import serializers, status, generics
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .permissions import IsAuthorOrReadOnly, IsAdminOrReadOnly, IsOwnerStuffOrReadOnly

from author.serializers import AuthorSerializer
from author.models import Author
from books.serializers import BookSerializer, FileSerializer, LanguageSerializer
from books.models import Book, Files, Language
from genre.serializers import GenreSerializer, TagSerializer, ContentWarningSerializer, AgeRatingSerializer
from genre.models import Genre, Tag, ContentWarning, AgeRating
from reactions.serializers import BookCommentsSerializer, BookScoreSerializer
from reactions.models import BookComments, BookScore
from users.serializers import UserSerializer


# ------------------Author API --------------------------------
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (IsAuthorOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# ------------------Books API --------------------------------
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsAuthorOrReadOnly, )
    ordering_fields = '__all__'
    # filterset_fields = ('authors', 'genres', 'tags',
    #                     'age_rating', 'warnings', 'user')
    search_fields = ('title', 'original_title', 'author__full_name',
                     'genre__name')
    filterset_fields = {
        'authors': ['exact', 'in'],
        'genres': ['exact', 'in'],
        'tags': ['exact', 'in'],
        'age_rating': ['exact', 'in'],
        'warnings': ['exact', 'in'],
        'user': ['exact'],
        'publication_year': ['exact', 'gte', 'lte'],
    }

    @action(detail=False, methods=['get'])
    def get_most_popular(self, request):
        books = self.get_queryset().order_by('-views_count')[:5:]
        serializer = self.get_serializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class LanguageViewSets(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = (IsAdminOrReadOnly, )


class FileViewSet(viewsets.ModelViewSet):
    queryset = Files.objects.all()
    serializer_class = FileSerializer
    permission_classes = (IsAuthorOrReadOnly,)

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
        serializer.save(book=book)


# ------------------Genres API --------------------------------
class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsAdminOrReadOnly, )


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (IsAdminOrReadOnly,)


class ContentWarningViewSet(viewsets.ModelViewSet):
    queryset = ContentWarning.objects.all()
    serializer_class = ContentWarningSerializer
    permission_classes = (IsAdminOrReadOnly,)


class AgeRatingViewSet(viewsets.ModelViewSet):
    queryset = AgeRating.objects.all()
    serializer_class = AgeRatingSerializer
    permission_classes = (IsAdminOrReadOnly,)


# ------------------Reactions API --------------------------------
class BookCommentViewSet(viewsets.ModelViewSet):
    serializer_class = BookCommentsSerializer
    queryset = BookComments.objects.all()
    permission_classes = (IsOwnerStuffOrReadOnly, )


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
        serializer.save(book=book)


class BookScoreViewSet(viewsets.ModelViewSet):
    serializer_class = BookScoreSerializer
    queryset = BookScore.objects.all()
    permission_classes = (IsOwnerStuffOrReadOnly, )

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

        serializer.save(book=book)


# ---------------------------- Register ---------------------------
class RegisterUserView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        headers = self.get_success_headers(serializer.data)

        token = RefreshToken().for_user(user)

        return Response(
            {
                'user': serializer.data,
                'refresh': str(token),
                'access': str(token.access_token),
            },
            status=status.HTTP_201_CREATED,
            headers=headers
        )