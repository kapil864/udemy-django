from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['text'].widget.attrs.update({'class': 'form-control','placeholder':'Leave a comment here'})
    
    class Meta:

        model = Comment
        exclude = ('movie',)
        
        labels = {
            'user_name' : 'Name',
            'text' : 'Comment'
        }