from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.


def month_challenges_by_numbers(request, month):
    return HttpResponse(month)

def month_challenges(request, month):
    content = None
    if month == 'january':
        content = 'This is a challenge for january'
    elif month == 'february':
        content = 'You made it to february.'
    if content:
        return HttpResponse(content)
    return HttpResponseNotFound('This is not supported')