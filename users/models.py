from django.contrib.auth.models import User
from django.db import models
from movies.models import Movie


def get_username(self):
    return "user" + self.username


User.add_to_class("__str__", get_username)


class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.SmallIntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):

        if len(Rating.objects.filter(user=self.user, movie=self.movie)):
            prev_rating = Rating.objects.get(user=self.user, movie=self.movie).rating
            self.movie.vote_average = (self.movie.vote_average * self.movie.vote_count - prev_rating + self.rating) / (
                self.movie.vote_count)
            self.movie.save()
        else:
            self.movie.vote_average = (self.movie.vote_average * self.movie.vote_count + self.rating) / (
                    self.movie.vote_count + 1)
            self.movie.vote_count += 1
            self.movie.save()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.movie.vote_count != 1:
            self.movie.vote_average = (self.movie.vote_average * self.movie.vote_count - self.rating) / (
                    self.movie.vote_count - 1)
        else:
            self.movie.vote_average = 0
        self.movie.vote_count -= 1
        self.movie.save()
        super().delete(*args, **kwargs)

    def __str__(self):
        return "user: {}, movie: {}, rating: {}".format(self.user, self.movie, self.rating)

    class Meta:
        unique_together = ('movie', 'user',)
