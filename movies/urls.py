from django.urls import path
from .views import movie_page
urlpatterns = [
    path('<str:slug>/', movie_page, name="movie_page_url"),
]
