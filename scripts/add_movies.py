from movies.models import Movie
import json


def add_movies():
    data = json.load(open('data/main_data.json', 'r', encoding='utf8'))
    step = 1
    for value in data:
        print(step, '/', len(data))
        m = Movie(title=value['title'],
                  original_title=value['original_title'],
                  tagline=value['tagline'],
                  imdb_id=value['imdb_id'],
                  release_date=value['release_date'],
                  overview=value['overview'],
                  poster_path=value['poster_path'],
                  backdrop_path=value['backdrop_path'])
        m.save()
        step += 1
