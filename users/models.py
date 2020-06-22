from django.contrib.auth.models import User


def get_username(self):
    return "user" + self.username


User.add_to_class("__str__", get_username)
