from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic import DetailView, FormView



from .forms import ReviewForm
from .models import Review

# Create your views here.

# CreateVIew 
# view will get forms
# validate it
# save it
class ReviewView(CreateView):

    model=Review
    form_class = ReviewForm
    template_name = 'reviews/review.html'
    success_url = '/thank-you'


# works for get requests
# returns template with context when a get request is received
class ThankYouView(TemplateView):
    template_name = 'reviews/thank_you.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['message'] = "This works and Thanks"
        return context


# Woks for get requests
# where a list of objects is required
# automatically fetches data from a defined model
class ReviewListView(ListView):

    template_name = 'reviews/review_list.html'

    # Define model
    model = Review

    # context name to be used in templates by default it is object_list
    context_object_name = 'reviews'

    # # Customizing query
    # def get_queryset(self) -> QuerySet[Any]:
    #     base_query = super().get_queryset()
    #     data = base_query.filter(rating__gt=1)
    #     return data


class SingleReviewView(DetailView):
    template_name = 'reviews/single_review.html'
    model = Review

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        loaded_review = self.object
        request = self.request
        favorite_id = request.session.get('favorite_review')
        context['is_favorite'] = favorite_id == str(loaded_review.id)
        return context


class AddFavoriteView(View):
    def post(self, request):

        # by default this review id received from HTML is a string
        review_id = request.POST['review_id']
        request.session['favorite_review'] = review_id
        return HttpResponseRedirect('/reviews/'+review_id)