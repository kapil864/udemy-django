from django import forms

from .models import CustomUser


class SignUpForm(forms.ModelForm):
  class Meta:
    model = CustomUser
    fields = ('username', 'email', 'password', 'phone_number', 'country_code')
    widgets = {
        'password': forms.PasswordInput(),  # Hide password input
    }
