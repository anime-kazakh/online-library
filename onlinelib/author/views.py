from django.shortcuts import render

from .models import Author

# Create your views here.
def index(request):
    data = {
        'authors': Author.objects.all(),
    }
    return render(request, 'author/index.html', context=data)

def author_page(request, author_slug):
    data = {
        'author': Author.objects.get(slug=author_slug)
    }
    return render(request, 'author/author_page.html', context=data)