
from django.db import models
from cloudinary.models import CloudinaryField


class Employee(models.Model):
    name = models.CharField(max_length=100, default='')
    photo = CloudinaryField('image')
    description = models.TextField(default='')
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50, default='')
    hire_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
