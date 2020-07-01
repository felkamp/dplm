from django.db.models import Avg
from recommender.scripts.similar_users import get_sim_users
from django.contrib.auth.models import User


def get_new_movies(user):
    sim_users = get_sim_users(user)
    if len(sim_users) and len(sim_users) != 1:
        movies_id = []
        for id_user in sim_users.keys():
            movies_id.extend(list(User.objects.get(id=id_user).rating_set.values_list("movie_id", flat=True)))

        movie_dict = {}
        for id in movies_id:
            if id in movie_dict:
                movie_dict[id] += 1
            else:
                movie_dict[id] = 1

        movie_list = list(movie_dict.items())
        movie_list.sort(key=lambda i: i[1], reverse=True)

        check_list = list(user.rating_set.values_list("movie_id", flat=True))
        return [x for x in movie_list if not x[0] in check_list and x[1] > 1], sim_users
    return [], []


def get_pred(user):
    new_movies, sim_users = get_new_movies(user)
    m = []
    if len(new_movies):
        user_avg = user.rating_set.aggregate(avg_rating=Avg("rating"))["avg_rating"]
        dividend = 0
        divisor = 0
        pred = []
        for movie in new_movies[:50]:
            for user_id in sim_users:
                an_user = User.objects.get(id=user_id)
                if an_user.rating_set.filter(movie_id=movie[0]).first() is not None:
                    nr_u = an_user.rating_set.get(movie_id=movie[0]).rating - \
                           an_user.rating_set.aggregate(avg_rating=Avg("rating"))[
                               "avg_rating"]
                    dividend += nr_u * sim_users[user_id]
                    divisor += sim_users[user_id]
            if divisor:
                pred_i = user_avg + dividend / divisor
                pred.append((movie[0], pred_i))
            dividend = 0
            divisor = 0

        pred.sort(key=lambda i: i[1], reverse=True)

        for movie_id in pred[:20]:
            m.append(str(movie_id[0]))
    return m
