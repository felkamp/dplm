from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Movie, Genre


# Create your views here.
def movie_page(request, slug):
    movie = get_object_or_404(Movie, slug__iexact=slug)
    user_rating = None
    similar_movies = []
    return render(request, 'movies/movie_page.html',
                  context={'movie': movie, 'similar_movies': similar_movies, 'user_rating': user_rating})


def genres_page(request):
    genres = Genre.objects.all().order_by("name")
    return render(request, 'movies/genres_page.html', context={'genres': genres})


def genre_page(request, slug):
    genre = Genre.objects.get(slug__iexact=slug)
    movies = genre.movies.all().filter(vote_count__gt=100).order_by("-vote_average", "-vote_count")[:50]
    return render(request, 'movies/movies_list.html', context={'movies': movies})
