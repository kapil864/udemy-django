from django.urls import path
from . import views


urlpatterns = [
    path('', view=views.index, name='index'),
    path('<int:month>', view=views.month_challenges_by_numbers),
    path('<str:month>', view=views.month_challenges, name='release-month')
]
