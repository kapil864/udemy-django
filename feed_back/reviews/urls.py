from django.urls import path
from . import views
urlpatterns = [
    path('', view=views.review),
    path('thank-you', view=views.thankyou)
]
