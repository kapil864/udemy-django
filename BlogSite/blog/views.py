from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from .models import Movie, Comment
from django.views import View
from django.views.generic import ListView, DetailView, CreateView
from .forms import CommentForm
from django.urls import reverse

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
    context_object_name = 'movies'


class ReleaseDetailView(View):

    def get(self, request, slug):
        try:
            movie = Movie.objects.get(slug=slug)
            comments = Comment.objects.filter(movie=movie)
            return render(request, 'blog/movie.html', {'movie': movie,'comments':comments, 'comment_form': CommentForm()})
        except:
            raise Http404()

    def post(self, request, slug):
        form = CommentForm(request.POST)
        movie = Movie.objects.get(slug=slug)
        if form.is_valid():
            # will not save to database immediately
            comment = form.save(commit=False)
            comment.movie = movie
            comment.save()
            return HttpResponseRedirect(reverse('a-release',args=[slug]))
        return render(request, 'blog/movie.html', {'movie': movie, 'comment_form': form})
