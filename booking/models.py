from django.db import models
import datetime

class Booking(models.Model):
    car = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    date = models.DateField(default=datetime.date.today)
    message = models.TextField(blank=True)
    
    def __str__(self):
        return str(self.name)
