import pytest
from django.contrib.auth.models import Group

from django.urls import reverse

from .factories import AuthorFactory
from ..models import Author


pytestmark = pytest.mark.django_db

class TestAuthorView:
    """
    Тестирование Views
    """

    # --------------- author-home --------------------
    def test_author_home(self, client):
        authors = AuthorFactory.create_batch(3)

        url = reverse('author-home')
        response = client.get(url)

        assert response.status_code == 200
        assert 'author/index.html' in response.template_name

        for _author in authors:
            assert _author.full_name in response.content.decode()

    # -------------- author-page ---------------------
    def test_author_page(self, client):
        author = AuthorFactory.create()
        url = reverse('author-page', kwargs={'author_slug': author.slug})
        response = client.get(url)
        assert response.status_code == 200
        assert 'author/author_page.html' in response.template_name
        assert author.full_name in response.content.decode()

    # ------------- login required -----------------------
    def test_addauthor_view_requires_login(self, client):
        url = reverse('add-author')
        response = client.get(url)
        assert response.status_code == 302
        redirect_url = reverse('users:login')
        assert redirect_url in response.url

    def test_addauthor_success(self, client, superuser):
        client.force_login(superuser)

        url = reverse('add-author')
        data = {
            'full_name': 'test_name',
            'slug': 'test_slug',
            'birth_date': '1970-01-01',
            'bio': 'test_bio',
        }

        response = client.post(url, data=data)

        assert response.status_code == 302
        redirect_url = reverse('author-page', kwargs={'author_slug': data['slug']})
        assert redirect_url in response.url
        assert Author.objects.filter(slug=data['slug']).exists()

    def test_updateauthor_view_required_login(self, client):
        author = AuthorFactory.create()
        url = reverse('update-author', kwargs={'slug': author.slug})
        response = client.get(url)
        assert response.status_code == 302
        redirect_url = reverse('users:login')
        assert redirect_url in response.url

    def test_updateauthor_success(self, client, superuser):
        author = AuthorFactory.create()
        url = reverse('update-author', kwargs={'slug': author.slug})

        client.force_login(superuser)

        data = {
            'full_name': author.full_name,
            'slug': author.slug,
            'birth_date': author.birth_date,
            'photo': author.photo,
            'bio': 'new test bio'
        }

        response = client.post(url, data=data)

        assert response.status_code == 302
        redirect_url = reverse('author-page', kwargs={'author_slug': author.slug})
        assert redirect_url in response.url
        assert Author.objects.get(slug=author.slug).bio == data['bio']

    def test_deleteauthor_view_required_login(self, client):
        author = AuthorFactory.create()
        url = reverse('delete-author', kwargs={'slug': author.slug})
        response = client.get(url)
        assert response.status_code == 302
        redirect_url = reverse('users:login')
        assert redirect_url in response.url

    def test_deleteauthor_success(self, client, superuser):
        author = AuthorFactory.create()
        url = reverse('delete-author', kwargs={'slug': author.slug})
        client.force_login(superuser)

        response = client.post(url)

        assert response.status_code == 302
        redirect_url = reverse('author-home')
        assert redirect_url in response.url
        assert not Author.objects.filter(slug=author.slug).exists()