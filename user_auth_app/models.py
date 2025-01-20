from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class UserProfile(models.Model):
    TYPE_CHOICES = [
        ("customer", "Customer"),
        ("business", "Business"),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    file = models.CharField(max_length=30, blank=True)
    location = models.CharField(max_length=30, blank=True)
    tel = models.CharField(max_length=30, blank=True)
    description = models.TextField(max_length=255, blank=True)
    working_hours = models.CharField(max_length=30, blank=True)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default="customer")
    

    def __str__(self):
        return f"{self.user.username} ({self.type})"
    
    def clean(self):
        super().clean()
        if self.type not in dict(self.TYPE_CHOICES).keys():
            raise ValueError("Invalid type selected.")