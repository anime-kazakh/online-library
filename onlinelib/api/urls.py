from django.urls import path, include

from rest_framework import routers
from rest_framework_nested.routers import NestedDefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from . import views


app_name = 'api'

router = routers.DefaultRouter()
# ---------Author API Path-------------
router.register(r'authors', views.AuthorViewSet)
# ---------Books API Path--------------
router.register(r'books', views.BookViewSet)
nested_router = NestedDefaultRouter(router, r'books', lookup='book')
nested_router.register(r'files', views.FileViewSet)
router.register(r'languages', views.LanguageViewSets)
# -------Reactions API Path------------
nested_router.register(r'comments', views.BookCommentViewSet)
nested_router.register(r'scores', views.BookScoreViewSet)
# ---------Genres API Path-------------
router.register('genres', views.GenreViewSet)
router.register('tags', views.TagViewSet)
router.register('contentwarnings', views.ContentWarningViewSet)
router.register('ageratings', views.AgeRatingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', include(nested_router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]