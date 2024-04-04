from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import login, logout
from django.views import View

from .forms import SignUpForm
# Create your views here.


class SignInView(View):

    def get(self, request):
        # default key for query parameter
        next = request.GET.get('next')
        if next != '':
            return render(request, 'accounts/login.html', {'next': next})
        return render(request, 'accounts/login.html')

    def post(self, request):

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            next = request.POST.get('next')
            if next != '':
                return redirect(next)
            return redirect(reverse('release-index'))
        else:
            messages.error(request, 'Bad credentials')
            return redirect(reverse('login'))


class SignOutView(View):

    def get(self, request):
        logout(request)
        return redirect(reverse('release-index'))


class SignUpView(View):

    def get(self, request):
        sign_up_form = SignUpForm()
        return render(request, 'accounts/signup.html',  {'sign_up_form': sign_up_form})

    def post(self, request):
        sign_up_form = SignUpForm(request.POST)
        if sign_up_form.is_valid():
            sign_up_form.save()
            messages.success(
                request, "Your account has been successfully create")
            return redirect(reverse('login'))
        return render(request, 'accounts/signup.html', {'sign_up_form': sign_up_form})
