from movies.models import Movie, Genre
import json


def add_genres():
    Genre.objects.create(name="приключения", slug="adventure")
    Genre.objects.create(name="мультфильм", slug="animation")
    Genre.objects.create(name="комедия", slug="comedy")
    Genre.objects.create(name="криминал", slug="crime")
    Genre.objects.create(name="документальный", slug="documentary")
    Genre.objects.create(name="драма", slug="drama")
    Genre.objects.create(name="семейный", slug="family")
    Genre.objects.create(name="фэнтези", slug="fantasy")
    Genre.objects.create(name="история", slug="history")
    Genre.objects.create(name="ужасы", slug="horror")
    Genre.objects.create(name="музыка", slug="music")
    Genre.objects.create(name="детектив", slug="mystery")
    Genre.objects.create(name="фантастика", slug="science-fiction")
    Genre.objects.create(name="телевизионный фильм", slug="tv-movie")
    Genre.objects.create(name="мелодрама", slug="romance")
    Genre.objects.create(name="триллер", slug="thriller")
    Genre.objects.create(name="военный", slug="war")
    Genre.objects.create(name="вестерн", slug="western")
    Genre.objects.create(name="боевик", slug="action")

    data = json.load(open('data/main_data.json', 'r', encoding='utf8'))
    step = 1
    for dct in data:
        print(step, "/", len(data))
        movie = Movie.objects.get(imdb_id=dct['imdb_id'])
        for genre in dct['genres']:
            g = Genre.objects.get(name=genre['name'])
            movie.genres.add(g)
        step += 1
