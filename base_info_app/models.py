from django.db import models

# Create your models here.

class BaseInfo(models.Model):
    review_count = models.IntegerField(default=0)
    average_rating = models.FloatField(default=0.0)
    business_profile_count = models.IntegerField(default=0)
    offer_count = models.IntegerField(default=0)