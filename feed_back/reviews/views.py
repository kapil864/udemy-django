from typing import Any
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView

from .forms import ReviewForm
from .models import Review

# Create your views here.

class ReviewView(View):

    def get(self, request):

        form = ReviewForm()
        return render(request, 'reviews/review.html', {'form':form})

    def post(self, request):
        
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thank-you')
        
        return render(request, 'reviews/review.html', {'form':form})
    


# works for get requests
# returns template with context when a get request is received
class ThankYouView(TemplateView):
    template_name = 'reviews/thank_you.html'
    
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['message'] = "This works and Thanks"
        return context
    

class ReviewListView(TemplateView):
    template_name = 'reviews/review_list.html'

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["reviews"] = Review.objects.all() 
        return context
    

class SingleReviewView(TemplateView):
    template_name = 'reviews/single_review.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        review_id = kwargs['id']
        context["review"] = Review.objects.get(pk=review_id)
        return context

    