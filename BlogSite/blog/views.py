from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Movie, Comment
from .forms import CommentForm

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
            return render(request, 'blog/movie.html', {'movie': movie, 'comments': comments, 'comment_form': CommentForm()})
        except:
            raise Http404()

    @method_decorator(login_required)
    def post(self, request, slug):
        form = CommentForm(request.POST)
        movie = Movie.objects.get(slug=slug)
        if form.is_valid():
            # will not save to database immediately
            comment = form.save(commit=False)
            comment.movie = movie
            comment.save()
            return HttpResponseRedirect(reverse('a-release', args=[slug]))
        return render(request, 'blog/movie.html', {'movie': movie, 'comment_form': form})


class WatchLaterView(LoginRequiredMixin, View):

    def get(self, request):
        stored_movies = request.session.get('stored_movies')
        context = {}

        if stored_movies is None or len(stored_movies) == 0:
            context['movies'] = []
            context['has_movies'] = False
        else:
            movies = Movie.objects.filter(id__in=stored_movies)
            print(movies)
            context['movies'] = movies
            context['has_movies'] = True

        return render(request, 'blog/watch_later.html', context=context)

    def post(self, request):
        stored_movies = request.session.get('stored_movies')

        if stored_movies is None:
            stored_movies = list()

        movie_id = int(request.POST['movie_id'])
        if movie_id not in stored_movies:
            stored_movies.append(movie_id)

        request.session['stored_movies'] = stored_movies
        return HttpResponseRedirect('/')
