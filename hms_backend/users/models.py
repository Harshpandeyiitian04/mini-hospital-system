from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    USER_ROLES=(
        ('doctor','Doctor'),
        ('patient','Patient'),

    )

    role=models.CharField(max_length=10,choices=USER_ROLES)
    email=models.EmailField(unique=True)

    def __str__(self):
        return self.username
    
class Patient(models.Model):
    user =models.OneToOneField(User,on_delete=models.CASCADE)
    phone =models.CharField(max_length=15)
    google_calendar_token =models.JSONField(null=True,blank=True)

    def __str__(self):
        return self.user.username