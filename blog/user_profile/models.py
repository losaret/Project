from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserFollower(models.Model):
    user = models.ForeignKey(User, unique=True, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    followers = models.ManyToManyField(User, related_name='followers')
    def __unicode__(self):
        return self.user

class UserFollowing(models.Model):
    user = models.ForeignKey(User, unique=True, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    followings = models.ManyToManyField(User, related_name='followings')
    def __unicode__(self):
        return self.user