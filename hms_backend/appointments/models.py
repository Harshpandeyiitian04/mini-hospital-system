from django.db import models
from doctors.models import AvailabilitySlot
from users.models import Patient

class Appointment(models.Model):
    patient =models.ForeignKey(Patient,on_delete=models.CASCADE)
    slot =models.OneToOneField(AvailabilitySlot,on_delete=models.CASCADE)
    created_at =models.DateTimeField(auto_now_add=True)
    google_event_id =models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return f"{self.patient} -> {self.slot}"