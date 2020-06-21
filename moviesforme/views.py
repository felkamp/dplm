from django.shortcuts import render
from movies.models import Movie


def main_page(request):
    new_movies = Movie.objects.all().order_by('-release_date')[:50]
    popular_movies = Movie.objects.filter(vote_count__gte=500).order_by('-vote_average')
    popular_movies = popular_movies.filter(vote_average__gte=7).order_by('-release_date')
    new_movies_clean = []
    popular_movies_clean = []
    for movie in new_movies:
        if movie.poster_path is not None:
            new_movies_clean.append(movie)
    for movie in popular_movies:
        if movie.poster_path is not None:
            popular_movies_clean.append(movie)
    new_movies = new_movies_clean[:10]
    popular_movies = popular_movies_clean[:10]
    return render(request, 'main_page.html', context={'popular': popular_movies, 'new': new_movies})
