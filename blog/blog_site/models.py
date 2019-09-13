from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class blog_post(models.Model):
    post_text = models.CharField(max_length=260)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField('created_date', default=timezone.now)
    def __str__(self):
        return self.post_text
