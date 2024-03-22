from django.shortcuts import render
from .models import movies_data
from django.http import Http404


# Create your views here.


def starting_page(request):
    try:
        latest_movies = movies_data[:-5:-1]
        return render(request, 'blog/welcome.html', {'latest_movies': latest_movies})
    except:
        return Http404()


def releases(request):
    try:
        return render(request, 'blog/list_movies.html', {'movies': movies_data})
    except:
        return Http404()


def release_detail(request, slug):
    try:
        movie = next(movie for movie in movies_data if movie['Title'] == slug)
        return render(request, 'blog/movie.html', {'movie': movie})
    except:
        return Http404()
