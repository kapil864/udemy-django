from django import forms
from .models import Review


# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label='Your name', max_length=100, error_messages= {
#         'required' : 'Name must not be empty',
#         'max_length' : 'Enter a shorter name '
#     } )

#     review = forms.CharField(label='Feed back', widget=forms.Textarea, max_length=100)
#     rating = forms.IntegerField(label='Rating', min_value= 1, max_value=5)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'  # ['user_name']
        # exclude = ['field to exclude']
        labels = {
            'user_name': 'Your name',
            'review': 'Your Review',
            'rating': 'Rating'
        }

        #custom error messages
        error_messages = {
            'user_name': {
                'required': 'Name must not be empty',
                'max_length': 'Enter a shorter name '
            }
        }
