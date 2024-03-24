from django.shortcuts import render
from .models import movies_data
from django.http import Http404
from .models import Movie
from django.views.generic import View
from django.views.generic import ListView, DetailView

# Create your views here.


class StaringView(View):

    def get(self, request):
        try:
            latest_movies = Movie.objects.all().order_by('-released')[0:2]
            return render(request, 'blog/welcome.html', {'latest_movies': latest_movies})
        except:
            raise Http404()

class ReleasesView(ListView):
    model = Movie
    template_name = 'blog/list_movies.html'
    context_object_name= 'movies'


class ReleaseDetailView(DetailView):
    model = Movie
    template_name = 'blog/movie.html'
    context_object_name = 'movie'
