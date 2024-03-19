from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def january(request):
    return HttpResponse("This is challenges.")


def february(request):
    return HttpResponse("YOU made it to february.")
