from django.db import models
from cloudinary.models import CloudinaryField
import datetime

class Car(models.Model):
    MAKE = (
        ('Audi', 'Audi'),
        ('Bmw', 'Bmw'),
        ('Ford', 'Ford'),
        ('Mazda', 'Mazda'),
        ('Toyota', 'Toyota'),
        ('Lexus', 'Lexus'),
    )
    make = models.CharField(max_length=50, choices=MAKE)
    model = models.CharField(max_length=50)
    price = models.IntegerField()
    FUEL_TYPE = (
        ('Petrol', 'Petrol'),
        ('Diesel', 'Diesel'),
        ('Hybrid', 'Hybrid'),
        ('Electric', 'Electric'),
    )
    fuel_type = models.CharField(max_length=50, choices=FUEL_TYPE)
    YEAR_CHOICES = [(r, r) for r in range(2005, datetime.date.today().year+1)]
    year = models.IntegerField(('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    BODY = (
        ('Saloon', 'Saloon'),
        ('Hatchback', 'Hatchback'),
        ('Coupe', 'Coupe'),
        ('Estate', 'Estate'),

    )
    body = models.CharField(max_length=50, choices=BODY)
    TRANSMISSION = (
        ('Manual', 'Manual'),
        ('Automatic', 'Automatic'),
    )
    transmmission = models.CharField(max_length=50, choices=TRANSMISSION)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    picture = CloudinaryField('image')

    def __str__(self):
        return self.make.choices
