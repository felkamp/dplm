from django.db.models import Avg, Count
from users.models import Rating
from django.contrib.auth.models import User


def pearson(cur_user, an_user):
    cur_user = cur_user.rating_set
    an_user = an_user.rating_set

    # получаем средние оценки пользователей
    cur_user_avg = cur_user.aggregate(avg_rating=Avg("rating"))["avg_rating"]
    an_user_avg = an_user.aggregate(avg_rating=Avg("rating"))["avg_rating"]

    # получаем id оцененных фильмов пользователями
    s1 = set([x['movie'] for x in cur_user.values("movie")])
    s2 = set([x['movie'] for x in an_user.values("movie")])

    # находим общие оцененные фильмы
    common_movies = s1 & s2

    # формула Пирсона
    dividend = 0
    divisor_cur = 0
    divisor_an = 0
    for movie in common_movies:
        # нормализуем оценки пользователей
        nr_cur = cur_user.get(movie_id=movie).rating - cur_user_avg
        nr_an = an_user.get(movie_id=movie).rating - an_user_avg

        dividend += nr_cur * nr_an
        divisor_cur += nr_cur ** 2
        divisor_an += nr_an ** 2

    divisor = (divisor_cur ** 0.5) * (divisor_an ** 0.5)
    if divisor:
        return dividend / divisor
    return 0


def get_sim_users(user):
    min = len(user.rating_set.values()) // 2
    if min >= 10:
        min = 5

    ratings = Rating.objects.filter(user=user)
    sim_users = list(Rating.objects.filter(movie__in=ratings.values("movie")) \
                     .values("user_id").annotate(inters=Count("user_id")) \
                     .filter(inters__gt=min).values_list("user_id", flat=True))
    sim_users.remove(user.id)

    if len(sim_users):
        pearson_list = {}
        for id_user in sim_users[:50]:
            prsn = pearson(user, User.objects.get(id=id_user))
            if prsn > 0.5:
                pearson_list[id_user] = prsn

        return pearson_list
    return []

