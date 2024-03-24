from django.urls import path
from . import views
urlpatterns = [
    path('', view=views.ReviewView.as_view()),
    path('thank-you', view=views.ThankYouView.as_view()),
    path('reviews', view=views.ReviewListView.as_view()),
    path('reviews/<int:pk>', view=views.SingleReviewView.as_view())
]
