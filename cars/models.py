from django.db import models
from cloudinary.models import CloudinaryField
import datetime

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
    price = models.IntegerField(null=False, blank=False)
    FUEL_TYPE = (
        ('Petrol', 'Petrol'),
        ('Diesel', 'Diesel'),
        ('Hybrid', 'Hybrid'),
        ('Electric', 'Electric'),
    )
    fuel_type = models.CharField(max_length=50, choices=FUEL_TYPE)
    engine_size = models.FloatField()
    YEAR_CHOICES = [(r, r) for r in range(2005, datetime.date.today().year+1)]
    year = models.IntegerField(('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    BODY = (
        ('Saloon', 'Saloon'),
        ('Hatchback', 'Hatchback'),
        ('Coupe', 'Coupe'),
        ('Estate', 'Estate'),
        ('SUV', 'SUV'),

    )
    body = models.CharField(max_length=50, choices=BODY)
    TRANSMISSION = (
        ('Manual', 'Manual'),
        ('Automatic', 'Automatic'),
    )
    transmmission = models.CharField(max_length=50, choices=TRANSMISSION)
    colour = models.CharField(max_length=50, null=False, blank=False, default='')
    owners = models.IntegerField(null=False, blank=False)
    milage = models.FloatField(null=False, blank=False)
    description = models.TextField(null=False, blank=False, default='')
    date = models.DateField(auto_now_add=True)
    picture = CloudinaryField('image')

    def __str__(self):
        return self.title

    