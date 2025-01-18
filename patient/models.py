from django.db import models
from django.utils import timezone
from userauths import models as userauths_models

# we created tuple here for every new appintment notification the doctor gets
NOTIFICATION_TYPE=(
    ("Appointment Scheduled", "Appointment Scheduled"),
    ("Appointment Cancelled", "Appointment Cancelled"),
)

# Create your models here.

class Patient(models.Model):
    user=models.OneToOneField(userauths_models.User, on_delete=models.CASCADE)
    image=models.ImageField(upload_to="images", null=True, blank=True)
    full_name=models.CharField(max_length=100, null=True, blank=True)
    email=models.CharField(max_length=100, null=True, blank=True)
    mobile=models.CharField(max_length=100, null=True, blank=True)
    adress=models.CharField(max_length=100, null=True, blank=True)
    gender=models.CharField(max_length=100, null=True, blank=True)
    dob=models.CharField(max_length=100, null=True, blank=True)
    blood_group=models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return f"{self.full_name}"


class Notification(models.Model):
    patient=models.ForeignKey(Patient,on_delete=models.SET_NULL, null=True, blank=True)
    appointment=models.ForeignKey("base.Appointment", on_delete=models.CASCADE, null=True, blank=True, related_name="patient_appointment_notification")
    type=models.CharField(max_length=100, choices=None)
    seen=models.BooleanField(default=False)
    date=models.DateField(auto_now_add=True)
    
 
class Meta:
    verbose_name_plural = "Notification"
def __str__(self):
    return f"{self.patient.full_name} Notification"