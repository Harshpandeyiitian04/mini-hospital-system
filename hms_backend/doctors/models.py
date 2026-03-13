from django.db import models
from django.conf import settings

User =settings.AUTH_USER_MODEL

class Doctor(models.Model):
    user =models.OneToOneField(User,on_delete=models.CASCADE)
    specialization =models.CharField(max_length=100)
    bio =models.TextField(blank=True)
    google_calendar_token =models.JSONField(null=True,blank=True)

    def __str__(self):
        return f"Dr. {self.user.username}"
    
class AvailabilitySlot(models.Model):
    doctor =models.ForeignKey(Doctor,on_delete=models.CASCADE)
    date =models.DateField()
    start_time =models.TimeField()
    end_time =models.TimeField()
    is_booked =models.BooleanField(default=False)

    def __str__(self):
        return f"{self.doctor} {self.date} {self.start_time}"