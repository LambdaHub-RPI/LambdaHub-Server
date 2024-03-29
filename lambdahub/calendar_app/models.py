from django.db import models

class Event(models.Model):
    name = models.CharField(max_length = 200)
    description = models.TextField()
    date = models.DateField()
    starttime = models.TimeField()
    endtime = models.TimeField()

    def __str__(self):
        return str(self.name)
    
    def save(self, *args, **kwargs):
        super().save(*args,**kwargs)
