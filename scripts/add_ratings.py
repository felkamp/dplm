from movies.models import Movie
from django.contrib.auth.models import User
from users.models import Rating
from django.db.models import Avg


def add_ratings():
    users = {}
    step = 1
    for u in User.objects.all():
        print(step, '/', User.objects.all().count())
        users[u.username] = u
        step += 1

    movies = {}
    step = 1
    for m in Movie.objects.all():
        print(step, '/', Movie.objects.all().count())
        movies[m.imdb_id] = m
        step += 1

    ratings = []
    step = 1
    for line in open('data/ratings.dat', 'r', encoding='utf8'):
        print(step, '/ 863435')
        rating_info = line.split('::')
        user_id = rating_info[0]
        movie_id = rating_info[1]
        rating = rating_info[2]

        if len(movie_id) < 7:
            movie_id = (7 - len(movie_id)) * '0' + movie_id
        movies_id = 'tt' + movie_id
        m = movies.get(movies_id, '')
        if m:
            ratings.append(Rating(movie=m, user=users[user_id], rating=int(rating)))
        step += 1
        if step % 50000 == 0:
            print('Занесение оценок в базу...')
            Rating.objects.bulk_create(ratings)
            ratings = []
    Rating.objects.bulk_create(ratings)

    print('Обновление средних рейтингов и количества голосов...')
    step = 1
    for m in Movie.objects.all():
        print(step, '/', Movie.objects.all().count())
        m.vote_count = m.rating_set.count()
        m.vote_average = m.rating_set.aggregate(avg_rating=Avg("rating"))["avg_rating"]
        m.save()
        step += 1
