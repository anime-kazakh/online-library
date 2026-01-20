menu = [
    { 'title': 'Жанры', 'url_name': 'genre-home' },
    { 'title': 'Авторы', 'url_name': 'author-home' },
    { 'title': 'Книги', 'url_name': 'books-home' },
    { 'title': 'О сайте', 'url_name': 'about' },
]

class DataMixin:
    title_page = None
    extra_context = {}

    def __init__(self):
        if self.title_page:
            self.extra_context['title'] = self.title_page

        if 'menu' not in self.extra_context:
            self.extra_context['menu'] = menu

    # def get_mixin_context(self, context, **kwargs):
    #     context['menu'] = self.extra_context['menu']
    #     context.update(kwargs)
    #     return context