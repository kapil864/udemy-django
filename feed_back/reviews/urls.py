from django.urls import path
from . import views
urlpatterns = [
    path('', view=views.ReviewView.as_view()),
    path('thank-you', view=views.thankyou)
]
