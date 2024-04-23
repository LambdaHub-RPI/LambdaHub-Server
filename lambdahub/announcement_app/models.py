from django.db import models

# Create your models here.
class Announcement(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    date = models.DateField()
    announcement = models.TextField()

    def __str__(self):
        return str(self.title)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
