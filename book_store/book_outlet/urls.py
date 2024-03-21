from django.urls import path

from . import views

urlpatterns = [
    path("", view=views.index),
    path('<int:id>', view = views.book_details, name='book-detail')
]
