# models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Offer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='offers', null=True, blank=True)
    title = models.CharField(max_length=255, default='default-title')
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class OfferDetail(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, related_name='details')
    title = models.CharField(max_length=255, default='default-title')
    revisions = models.PositiveIntegerField(default=-1)
    delivery_time_in_days = models.PositiveIntegerField(default=7)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    features = models.JSONField(default='default-feature')  # Speichert Features als JSON-Array
    offer_type = models.CharField(max_length=50, choices=[
        ('basic', 'Basic'),
        ('standard', 'Standard'),
        ('premium', 'Premium')
    ], default='basic')

    def __str__(self):
        return f"{self.title} - {self.offer.title}"
    