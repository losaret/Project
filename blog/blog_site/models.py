from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class blog_post(models.Model):
    post_text = models.CharField(max_length=260)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField('created_date', default=timezone.now)
    post_image = models.ImageField(upload_to='uploads/', null=True, blank=True)
    def __str__(self):
        return self.post_text

class Hashtag(models.Model):
    """ Hashtag model"""
    name = models.CharField(max_length=64, unique=True)
    post = models.ManyToManyField(blog_post)
    def _unicode(self):
        return self.name
