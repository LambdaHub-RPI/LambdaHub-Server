from django.db import models
from django.utils import timezone

class Ride(models.Model):
    name = models.CharField(max_length = 200)
    startlocation = models.TextField()
    endlocation = models.TextField()
    numPassengers = models.IntegerField()
    rideTime = models.TimeField(default=timezone.now)
    identifier = models.IntegerField()

    def __str__(self):
        return str(self.name)
    
    def save(self, *args, **kwargs):
        super().save(*args,**kwargs)
