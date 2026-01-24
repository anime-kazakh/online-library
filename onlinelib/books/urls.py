from django.urls import path

from . import views


urlpatterns = [
    path('', views.BookHome.as_view(), name='books-home'),
    path('addbook/', views.AddBook.as_view(), name='add-book'),
    path('addfile/', views.AddFile.as_view(), name='add-file'),
    # path('addlanguage/', views.AddLanguage.as_view(), name='add-language'),
    path('editbook/<slug:slug>/', views.UpdateBook.as_view(), name='edit-book'),
    path('editfile/<int:pk>/', views.UpdateFile.as_view(), name='edit-file'),
    # path('editlanguage/<int:pk>/', views.UpdateLanguage.as_view(), name='edit-language'),
    path('deletebook/<slug:slug>/', views.DeleteBook.as_view(), name='delete-book'),
    path('deletefile/<int:pk>/', views.DeleteFile.as_view(), name='delete-file'),
    path('filedownload/<int:file_id>/', views.file_download, name='file-download'),
    path('<slug:book_slug>/', views.BookPage.as_view(), name='book-page'),
]