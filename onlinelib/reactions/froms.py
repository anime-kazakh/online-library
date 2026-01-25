from django import forms

from .models import BookComments


class CommentForm(forms.ModelForm):
    class Meta:
        model = BookComments
        fields = ['comment']
        widgets = {
            'comment': forms.Textarea(attrs={
                'class': 'comment-area',
                'rows': 5,
                'placeholder': 'Ваш комментарий',
            }),
        }