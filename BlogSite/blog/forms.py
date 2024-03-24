from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    
    class Meta:

        model = Comment
        exclude = ('movie',)
        
        labels = {
            'user_name' : 'Name',
            'text' : 'Comment'
        }