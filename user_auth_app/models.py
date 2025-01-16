from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class UserProfile(models.Model):
    ROLE_CHOICES = [
        ("customer", "Customer"),
        ("provider", "Provider"),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return self.user.username
