from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time
import random


def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time() + random.randrange(2, 50)))


class Movie(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    original_title = models.CharField(max_length=250)
    tagline = models.CharField(max_length=250, blank=True)
    slug = models.SlugField(max_length=200, blank=True)
    imdb_id = models.CharField(max_length=20)
    genres = models.ManyToManyField('Genre', blank=True, related_name='movies')
    keywords = models.ManyToManyField('Keyword', blank=True, related_name='movies')
    release_date = models.DateField()
    date_pub = models.DateTimeField(auto_now_add=True)
    overview = models.TextField(blank=True)
    poster_path = models.URLField(max_length=200, blank=True, null=True)
    backdrop_path = models.URLField(max_length=200, blank=True, null=True)
    vote_average = models.FloatField(blank=True, default=0, null=True)
    vote_count = models.IntegerField(blank=True, default=0, null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movie_page_url', kwargs={'slug': self.slug})


class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('genre_page_url', kwargs={'slug': self.slug})


class Keyword(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
