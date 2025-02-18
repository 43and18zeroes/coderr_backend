from django.db import models
from django.contrib.auth.models import User
from django.db.models import Min

class Offer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='offers', null=True, blank=True)
    title = models.CharField(max_length=255, default='default-title')
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='offer_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    min_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    min_delivery_time = models.PositiveIntegerField(default=7)
    
    def update_min_price(self, save_instance=True):
        min_price = self.details.aggregate(Min('price'))['price__min']
        new_min_price = min_price if min_price is not None else 0.0
        
        if self.min_price != new_min_price:
            self.min_price = new_min_price
            if save_instance:
                super().save(update_fields=['min_price'])

    def update_min_delivery_time(self, save_instance=True):
        min_delivery_time = self.details.aggregate(Min('delivery_time_in_days'))['delivery_time_in_days__min']
        new_min_delivery_time = min_delivery_time if min_delivery_time is not None else 7
        
        if self.min_delivery_time != new_min_delivery_time:
            self.min_delivery_time = new_min_delivery_time
            if save_instance:
                super().save(update_fields=['min_delivery_time'])

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.update_min_price(save_instance=False)
        self.update_min_delivery_time(save_instance=False)

    def __str__(self):
        return self.title


class OfferDetail(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, related_name='details')
    title = models.CharField(max_length=255, default='default-title')
    revisions = models.PositiveIntegerField(default=-1)
    delivery_time_in_days = models.PositiveIntegerField(default=7)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    features = models.JSONField(default=dict)
    offer_type = models.CharField(max_length=50, choices=[
        ('basic', 'Basic'),
        ('standard', 'Standard'),
        ('premium', 'Premium')
    ], default='basic')
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.offer.update_min_price()
        self.offer.update_min_delivery_time()

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        self.offer.update_min_price()
        self.offer.update_min_delivery_time()

    def __str__(self):
        return f"{self.title} - {self.offer.title}"