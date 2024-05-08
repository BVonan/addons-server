from django.db import models

# Create your models here.
from django.utils import timezone
import datetime

from django.contrib.auth.models import User


class Ads(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Downloads(models.Model):
    question = models.ForeignKey(Ads, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
    

class AdTracking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ad_id = models.CharField(max_length=100)
    clicks = models.PositiveIntegerField(default=0)
    downloads = models.PositiveIntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    

