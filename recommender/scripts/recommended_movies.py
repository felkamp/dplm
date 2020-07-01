from recommender.scripts.pred import get_pred
from movies.models import Movie
from recommender.models import Recommendation
import random


def get_popular_movies(user):
    recommended_movies = Movie.objects.filter(vote_count__gte=500).order_by('-vote_average').filter(vote_average__gte=7)
    not_rated = [movie for movie in recommended_movies if
                 movie.id not in user.rating_set.values_list("movie_id", flat=True)]
    random.shuffle(not_rated)
    recommended_movies = not_rated[:10]
    return recommended_movies


def update_rec(user, rec_type):
    rec_movies_id = get_pred(user)
    rec_id = getattr(user.recommendation, rec_type)
    if len(rec_movies_id) == 0:
        pop_movies = get_popular_movies(user)
        pop_movies = list(map(str, list(pop_movies.values_list('id', flat=True))))
        rec_id.extend(pop_movies)
    else:
        rec_id.extend(rec_movies_id)
    user_rec = Recommendation.objects.get(user=user)
    if rec_type == 'svd':
        user_rec.svd = rec_id
    elif rec_type == 'user_based':
        user_rec.user_based = rec_id
    user_rec.save()


def get_rec_movies(user):
    recommended_movies = []
    try:
        if user.recommendation.svd:
            if len(user.recommendation.svd) == 10:
                update_rec(user, 'svd')
            recommended_movies = [Movie.objects.get(id=id) for id in user.recommendation.svd[:10]]
        elif user.recommendation.user_based:
            if len(user.recommendation.user_based) == 10:
                update_rec(user, 'user_based')
            recommended_movies = [Movie.objects.get(id=id) for id in user.recommendation.user_based[:10]]
    except Recommendation.DoesNotExist:
        if user.rating_set.count() >= 5:
            rec_movies_id = get_pred(user)
            if len(rec_movies_id) > 9:
                Recommendation.objects.create(user=user, user_based=rec_movies_id)
                recommended_movies = [Movie.objects.get(id=id) for id in rec_movies_id[:10]]
            else:
                recommended_movies = get_popular_movies(user)
        else:
            recommended_movies = get_popular_movies(user)
    return recommended_movies
