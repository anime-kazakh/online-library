from django.shortcuts import render


menu = [
    { 'title': 'Главная страница', 'url_name': 'home' },
    { 'title': 'О себе', 'url_name': 'about' },
]

def index(request):
    data = {
        'menu': menu,
    }
    return render(request, 'home/index.html', context=data)

def about(request):
    data = {
        'menu': menu,
    }
    return render(request, 'home/about.html', context=data)