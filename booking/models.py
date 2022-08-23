from django.db import models

class Booking(models.Model):
    car = models.CharField(max_length=100)
    car_id = models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    user_id = models.IntegerField(blank=True)
    
    def __str__(self):
        return str(self.name)
