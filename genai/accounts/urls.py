from django.urls import path
from .views import SignUpView, SignInView, SignOutView

urlpatterns = [
    path('login', SignInView.as_view(), name='login'),
    path('logout', SignOutView.as_view(), name='logout'),
    path('register', SignUpView.as_view(), name='register')
]
