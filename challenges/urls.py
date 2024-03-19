from django.urls import path
from . import views


urlpatterns = [
    path('january', view=views.january),
    path('february', view=views.february)
]
