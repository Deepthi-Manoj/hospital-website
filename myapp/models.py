from django.db import models

# Create your models here.
class Doctor(models.Model):
    Name=models.CharField(max_length=50)
    mobile = models.CharField(max_length=15, null=True) 
    special=models.CharField(max_length=50)



class Patient(models.Model):
    Name=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    mobile=models.IntegerField(null=True)
    adress=models.CharField(max_length=200)


class Appoinment(models.Model):
    Doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    Patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    Date=models.DateField()
    Time=models.TimeField()
