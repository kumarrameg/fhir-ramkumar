from django.db import models

class Patient(models.Model):
    """
    Represents a patient.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    address = models.CharField(max_length=200,null=True)
    city = models.CharField(max_length=100,null=True)
    state = models.CharField(max_length=100,null=True)
    country = models.CharField(max_length=100,null=True)




class Encounter(models.Model):
    """
    Represents an encounter with a patient.
    """
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    location = models.CharField(max_length=100)


class Observation(models.Model):
    """
    Represents an observation made during an encounter.
    """
    encounter = models.ForeignKey(Encounter, on_delete=models.CASCADE)
    observation_type = models.CharField(max_length=100)
    result = models.CharField(max_length=100)
