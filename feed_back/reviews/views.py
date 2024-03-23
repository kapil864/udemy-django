from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import ReviewForm
from .models import Review

# Create your views here.
def review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            review = Review(
                user_name = form.cleaned_data['user_name'],
                review = form.cleaned_data['review'],
                rating= form.cleaned_data['rating']
            )
            review.save()
            return HttpResponseRedirect('/thank-you')
    else:
        form = ReviewForm()
        
    return render(request, 'reviews/review.html', {'form':form})


def thankyou(request):
    return render(request, 'reviews/thank_you.html')