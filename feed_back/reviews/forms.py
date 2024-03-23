from django import forms

class ReviewForm(forms.Form):
    user_name = forms.CharField(label='Your name', max_length=100, error_messages= {
        'required' : 'Name must not be empty',
        'max_length' : 'Enter a shorter name '
    } )