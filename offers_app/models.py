# models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Offer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='offers', null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    min_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    min_delivery_time = models.PositiveIntegerField(default=7)

    def __str__(self):
        return self.title

class OfferDetail(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, related_name='details')
    url = models.URLField()

    def __str__(self):
        return f"Detail for Offer {self.offer.id}"
