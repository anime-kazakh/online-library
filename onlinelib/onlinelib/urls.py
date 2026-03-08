"""
URL configuration for onlinelib project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from debug_toolbar.toolbar import debug_toolbar_urls

from onlinelib import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('books/', include('books.urls')),
    path('authors/', include('author.urls')),
    path('genres/', include('genre.urls')),
    path('users/', include('users.urls', namespace='users')),
    path('reactions/', include('reactions.urls', namespace='reactions')),
    path('api/v1/', include('api.urls', namespace='api')),
] + debug_toolbar_urls()

admin.site.site_header = "Панель администрирования"
admin.site.index_title = "Администрирование сайта"

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)