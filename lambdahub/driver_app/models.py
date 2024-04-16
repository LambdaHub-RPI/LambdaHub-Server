from django.db import models
from django.utils import timezone
import random

class Ride(models.Model):
    name = models.CharField(max_length = 200)
    startlocation = models.TextField()
    endlocation = models.TextField()
    numPassengers = models.IntegerField()
    rideTime = models.TimeField(auto_now_add=True)
    identifier = models.IntegerField(default=random.randint(1, 10000))

    isEmergency = models.BooleanField(default=False)  # Add this line


    def __str__(self):
        return str(self.name)
    
    def save(self, *args, **kwargs):
        super().save(*args,**kwargs)
