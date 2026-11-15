from django.db import models

# Create your models here.
class Appointment(models.Model):
    name=models.CharField(max_length=200)

    phone=models.CharField(max_length=15)

    email=models.EmailField()

    doctor=models.IntegerField()

    appointment_date=models.DateField()

    appointment_time=models.TimeField()

    appointment_end_time=models.TimeField()

    duration=models.IntegerField()

    token=models.IntegerField()

    