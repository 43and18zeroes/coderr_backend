# models.py
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Min

class Offer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='offers', null=True, blank=True)
    title = models.CharField(max_length=255, default='default-title')
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    min_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    
    def update_min_price(self, save_instance=True):
        """Aktualisiert `min_price`, speichert aber nur, wenn es nötig ist."""
        min_price = self.details.aggregate(Min('price'))['price__min']
        new_min_price = min_price if min_price is not None else 0.0
        
        if self.min_price != new_min_price:  # Nur speichern, wenn sich der Wert ändert
            self.min_price = new_min_price
            if save_instance:
                super().save(update_fields=['min_price'])  # Speichert nur `min_price`

    def save(self, *args, **kwargs):
        """Standard-Save ohne `update_min_price`, um Rekursion zu vermeiden."""
        super().save(*args, **kwargs)  # Speichert das Offer
        self.update_min_price(save_instance=False)  # Berechnet `min_price`, aber speichert es nicht sofort

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
    
    def save(self, *args, **kwargs):
        """Speichert `OfferDetail` und aktualisiert `min_price` des zugehörigen `Offer`, aber ohne Rekursion."""
        super().save(*args, **kwargs)
        self.offer.update_min_price()

    def delete(self, *args, **kwargs):
        """Löscht `OfferDetail` und aktualisiert `min_price` des zugehörigen `Offer`."""
        super().delete(*args, **kwargs)
        self.offer.update_min_price()

    def __str__(self):
        return f"{self.title} - {self.offer.title}"
    