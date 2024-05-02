from django.shortcuts import render, redirect
from django.views import View

from .forms import SignUpForm
# Create your views here.

class SignUpView(View):

    def get(self, request):
        signup_form = SignUpForm()
        return render(request, 'accounts/signup.html', {'signup_form': signup_form})

    def post(self, request):
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            return render(request, 'accounts/signup_success.html')
        else:
            return render(request, 'accounts/signup.html', {'signup_form': signup_form})
        
class SignInView(View):

    def get(self, request):
        return render(request, 'accounts/signin.html')

    def post(self, request):
        pass


class SignOutView(View):

    def get(self, request):
        pass

    def post(self, request):
        pass
