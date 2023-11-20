from django.urls import path
from . import views

urlpatterns = [
    path('getmovies/', views.getMovies),
    path('getgenres/', views.getGenres),

]
