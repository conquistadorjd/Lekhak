from .models import Comment
from django import forms
from captcha.fields import CaptchaField

class CommentForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Comment
        fields = ('comment_author', 'comment_author_email', 'comment_content')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['comment_author'].widget.attrs.update({'class': 'form-control'})
        self.fields['comment_author_email'].widget.attrs.update({'class': 'form-control'})
        self.fields['comment_content'].widget.attrs.update({'class': 'form-control'})