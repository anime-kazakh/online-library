from django.shortcuts import render

from .models import Author
from .forms import AuthorForm

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

def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else: form = AuthorForm()

    data = {
        'form': form,
    }
    return render(request, 'author/add_author.html', context=data)