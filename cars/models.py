from django.db import models
from cloudinary.models import CloudinaryField
# import datetime

class Car(models.Model):
    title = models.CharField(max_length=300, null=False, blank=False, default='')
    MAKE = [
        ('Audi', 'Audi'),
        ('Bmw', 'Bmw'),
        ('Citroën', 'Citroën'),
        ('Ford', 'Ford'),
        ('Mazda', 'Mazda'),
        ('Skoda', 'Skoda'),
        ('Toyota', 'Toyota'),
        ('Opel', 'Opel'),
        ('Lexus', 'Lexus'),
        ('Mercedes', 'Mercedes'),
        ('Volkswagen', 'Volksvagen'),
        ('Volvo', 'Volvo'),
    ]
    make = models.CharField(max_length=50, choices=MAKE)
    model = models.CharField(max_length=50)
    picture = CloudinaryField('image')

    def __str__(self):
        return self.title

    