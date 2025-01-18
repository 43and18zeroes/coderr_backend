from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class UserProfile(models.Model):
    TYPE_CHOICES = [
        ("customer", "Customer"),
        ("business", "Business"),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default="customer")

    def __str__(self):
        return f"{self.user.username} ({self.type})"
    
    def clean(self):
        super().clean()
        if self.type not in dict(self.TYPE_CHOICES).keys():
            raise ValueError("Invalid type selected.")