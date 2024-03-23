from django.shortcuts import render
from .models import movies_data
from django.http import Http404
from .models import Movie

# Create your views here.


def starting_page(request):
    try:
        latest_movies = Movie.objects.all().order_by('-released')[0:2]
        return render(request, 'blog/welcome.html', {'latest_movies': latest_movies})
    except:
        raise Http404()


def releases(request):
    try:
        movies_data = Movie.objects.all()
        return render(request, 'blog/list_movies.html', {'movies': movies_data})
    except:
        raise Http404()


def release_detail(request, slug):
    try:
        movie = Movie.objects.get(slug=slug)
        return render(request, 'blog/movie.html', {'movie': movie})
    except:
        raise Http404()
