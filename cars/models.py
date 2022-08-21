import datetime
from django.db import models
from cloudinary.models import CloudinaryField
from employees.models import Employee

class Car(models.Model):
    sales_person = models.ForeignKey(Employee, on_delete=models.DO_NOTHING, default=True)
    title = models.CharField(max_length=300, null=False, blank=False, default='')
    MAKE = (
        ('Audi', 'Audi'),
        ('Bmw', 'Bmw'),
        ('Citroen', 'Citroen'),
        ('Ford', 'Ford'),
        ('Mazda', 'Mazda'),
        ('Skoda', 'Skoda'),
        ('Toyota', 'Toyota'),
        ('Opel', 'Opel'),
        ('Lexus', 'Lexus'),
        ('Mercedes', 'Mercedes'),
        ('Volkswagen', 'Volksvagen'),
        ('Volvo', 'Volvo')
    )
    make = models.CharField(max_length=50, choices=MAKE, default=MAKE[0][0])
    model = models.CharField(max_length=50)
    price = models.IntegerField(default=1)
    FUEL_TYPE = (
        ('Petrol', 'Petrol'),
        ('Diesel', 'Diesel'),
        ('Hybrid', 'Hybrid'),
        ('Electric', 'Electric')
    )
    fuel_type = models.CharField(max_length=50, choices=FUEL_TYPE, default=FUEL_TYPE[0][0])
    TRANSMISSION = (
        ('Manual', 'Manual'),
        ('Automatic', 'Automatic')
    )
    transmission = models.CharField(max_length=50, choices=TRANSMISSION, default=TRANSMISSION[0][0])
    BODY_TYPE = (
        ('Coupe', 'Coupe'),
        ('Saloon', 'Saloon'),
        ('Hatchback', 'Hatchback'),
        ('Estate', 'Estate'),
        ('SUV', 'SUV')
    )
    body_type = models.CharField(max_length=50, choices=BODY_TYPE, default=BODY_TYPE[0][0])
    YEAR_CHOICES = [(r, r) for r in range(2010, datetime.date.today().year+1)]
    year = models.IntegerField(('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    ENGINE_SIZE = (
        ('1.0L', '1.0L'),
        ('1.1L', '1.1L'),
        ('1.2L', '1.2L'),
        ('1.3L', '1.3L'),
        ('1.4L', '1.4L'),
        ('1.5L', '1.5L'),
        ('1.6L', '1.6L'),
        ('1.7L', '1.7L'),
        ('1.8L', '1.8L'),
        ('1.9L', '1.9L'),
        ('2.0L', '2.0L'),
        ('2.5L', '2.5L'),
        ('3.0L', '3.0L'),
        ('3.5L', '3.5L'),
        ('4.0L', '4.0L'),
        ('5.0L', '5.0L'),
    )
    engine_size = models.CharField(max_length=20, choices=ENGINE_SIZE, default=ENGINE_SIZE[0][0])
    milage = models.IntegerField(default=1)
    description = models.TextField(default='')
    previous_owners = models.IntegerField(default=1)
    road_tax = models.IntegerField(default=1)
    nct = models.DateField(auto_now=True)
    is_for_sale = models.BooleanField(default=True)
    photo_main = CloudinaryField('image') 
    photo_1 = CloudinaryField('image', blank=True)
    photo_2 = CloudinaryField('image', blank=True)
    photo_3 = CloudinaryField('image', blank=True)
    photo_4 = CloudinaryField('image', blank=True)
    photo_5 = CloudinaryField('image', blank=True)
    photo_6 = CloudinaryField('image', blank=True)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    