from django.urls import path
from .views import *

urlpatterns = [
    path('genres/', genres_page, name='genres_page_url'),
    path('genres/<str:slug>', genre_page, name='genre_page_url'),
    path('<str:slug>/', movie_page, name='movie_page_url'),
]
