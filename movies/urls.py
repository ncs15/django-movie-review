from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from movies import views as movie_views

urlpatterns = [
    path('', movie_views.movie_colection, name="movie_search"),
    path('coming-next/', movie_views.coming_next, name="coming_next"),
    path('popular/', movie_views.popular, name="popular"),
    path('action/', movie_views.movie_action, name="movie_action"),
    path('comedy/', movie_views.movie_comedy, name="movie_comedy"),
    path('animation/', movie_views.movie_animation, name="movie_animation"),
    path('adventure/', movie_views.movie_animation, name="movie_adventure"),
    path('classics/', movie_views.movie_classic, name="movie_classics"),
    path('crime/', movie_views.movie_crime, name="movie_crime"),
    path('dramas/', movie_views.movie_dramas, name="movie_dramas"),
    path('family/', movie_views.movie_family, name="movie_family"),
    path('fantasy/', movie_views.movie_fantasy, name="movie_fantasy"),
    path('romance/', movie_views.movie_romance, name="movie_romance"),
    path('sci-fi/', movie_views.movie_scifi, name="movie_sci-fi"),
    path('sports/', movie_views.movie_sports, name="movie_sports"),
    path('thriller/', movie_views.movie_thrille, name="movie_thriller"),
    path('biographical/', movie_views.movie_biographical, name="movie_biographical"),
    path('detail/<url>', movie_views.detail, name="movie_detail"),
]
