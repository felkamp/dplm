import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "moviesforme.settings")
django.setup()

from scripts.add_movies import add_movies
from scripts.add_genres import add_genres
import argparse


def main(object_name):
    exec('add_' + args.add + '()')
    print('Объекты добавлены')


if __name__ == '__main__':
    allowed_commands = ['movies', 'genres', 'users', 'keywords', 'ratings']
    parser = argparse.ArgumentParser(description='Добавление объекта в базу данных')
    parser.add_argument('-add', type=str, help='adding object in database')
    args = parser.parse_args()
    if args.add in allowed_commands:
        main(args.add)
    else:
        print('Введите комманду из списка [movies, genres, users, keywords, ratings]')
