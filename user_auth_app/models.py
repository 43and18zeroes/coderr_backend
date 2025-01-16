from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class UserProfile(models.Model):
    ROLE_CHOICES = [
        ("customer", "Customer"),
        ("provider", "Provider"),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="customer")

    def __str__(self):
        return f"{self.user.username} ({self.role})"
    
    def clean(self):
        super().clean()
        if self.role not in dict(self.ROLE_CHOICES).keys():
            raise ValueError("Invalid role selected.")