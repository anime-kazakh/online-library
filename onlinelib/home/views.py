from django.shortcuts import render


data = {
    'logo': { 'title': 'Главная страница', 'url_name': 'home' },
    'menu': [
        { 'title': 'О себе', 'url_name': 'about' },
        { 'title': 'Книги', 'url_name': 'books' },
    ],
}

def index(request):
    _context = {  }
    _context.update(data)
    return render(request, 'home/index.html', context=_context)

def about(request):
    _context = {}
    _context.update(data)
    return render(request, 'home/about.html', context=_context)