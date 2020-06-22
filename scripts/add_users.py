from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


def add_users():
    User.objects.bulk_create(
        [User(username=str(id), password=make_password(str(id), None, 'md5')) for id in range(1, 67310)])
