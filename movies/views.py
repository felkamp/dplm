from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Movie


# Create your views here.
def movie_page(request, slug):
    movie = get_object_or_404(Movie, slug__iexact=slug)
    user_rating = None
    similar_movies = []
    return render(request, 'movies/movie_page.html',
                  context={'movie': movie, 'similar_movies': similar_movies, 'user_rating': user_rating})
