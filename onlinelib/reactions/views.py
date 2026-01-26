from django.core.exceptions import ValidationError
from django.db.models import Avg
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

import json

from books.models import Book
from .models import BookComments, BookScore
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
                    'comment_id': book_comment.id,
                    'comment': book_comment.comment,
                    'post_time': book_comment.post_time.strftime('%Y.%m.%d %H:%M'),
                }
            })
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})


@login_required(login_url='/accounts/login/')
@require_POST
@csrf_exempt
def delete_book_comment(request):
    try:
        data = json.loads(request.body)
        comment_id = data['comment_id']
        comment = BookComments.objects.get(id=comment_id)

        if comment.user == request.user:
            comment.delete()
        else:
            raise ValidationError('This is not your comment')

        return JsonResponse({'success': True})

    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})


@login_required(login_url='/accounts/login/')
@require_POST
@csrf_exempt
def book_rate(request):
    try:
        data = json.loads(request.body)
        book = data['book']
        score = data['score']
        book_score = BookScore.existing.get_or_none(user=request.user, book=book)

        if book_score:
            book_score.score = score
            book_score.save()
        else:
            BookScore.objects.create(user=request.user, book=book, score=score)

        avg_score = BookScore.objects.filter(book=book).aggregate(Avg('score'))['score__avg']

        return JsonResponse({
            'success': True,
            'avg_score': round(avg_score, 1)
        })

    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})