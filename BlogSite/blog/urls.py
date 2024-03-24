from django.urls import path
from . import views

urlpatterns = [
    path('', views.StaringView.as_view(), name='release-index'),
    path('releases/', views.ReleasesView.as_view(), name='all-releases'),
    path('releases/watch-later', views.WatchLaterView.as_view(), name='watch-later'),
    path('releases/<slug:slug>', views.ReleaseDetailView.as_view(), name='a-release')
]
