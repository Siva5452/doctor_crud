from django.db import models

# Create your models here.
class Doctor(models.Model):
    name=models.CharField(max_length=200)
    specilaization=models.CharField(max_length=200)
    experience=models.PositiveIntegerField()
    fee=models.PositiveIntegerField()
    