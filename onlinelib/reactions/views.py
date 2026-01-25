from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

import json

from books.models import Book
from .models import BookComments
from .froms import CommentForm


@login_required(login_url='/accounts/login/')
@require_POST
@csrf_exempt
def add_book_comment(request):
    try:
        data = json.loads(request.body)
        book = data['book']
        comment = data['comment']

        form = CommentForm({'comment': comment})

        if form.is_valid():
            book_comment = BookComments.objects.create(book=Book.objects.get(id=book),
                                                       comment=comment,
                                                       user=request.user)
            return JsonResponse({
                'success': True,
                'BookComment': {
                    'book': book,
                    'user': request.user.username,
                    'comment': book_comment.comment,
                    'post_time': book_comment.post_time.strftime('%Y/%m/%d %H:%M'),
                }
            })
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})