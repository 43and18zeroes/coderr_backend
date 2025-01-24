from django.contrib.auth.models import User
from django.db import models

class Review(models.Model):
    business_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews_received")
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews_given")
    rating = models.PositiveIntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Review {self.id} - Rating: {self.rating}"