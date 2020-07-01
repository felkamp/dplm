from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class Recommendation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    svd = ArrayField(models.CharField(max_length=10), blank=True, null=True)
    user_based = ArrayField(models.CharField(max_length=10), blank=True, null=True)

    def __str__(self):
        return 'user' + self.user.username
