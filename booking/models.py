from django.db import models
from django.contrib.auth.models import User
import datetime

class Booking(models.Model):
    car = models.CharField(max_length=100)
    car_id = models.IntegerField(default=0)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    date = models.DateField(default=datetime.date.today)
    message = models.TextField(blank=True)
    user_id = models.IntegerField(default=0)
    
    
    def __str__(self):
        return str(self.name)
