from django.urls import path
from . import views

urlpatterns = [
    path('',views.starting_page,name='release-index'),
    path('releases/',views.releases, name='all-releases'),
    path('releases/<str:slug>',views.release_detail, name='a-release')
]
