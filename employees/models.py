from django.db import models
from cloudinary.models import CloudinaryField

class Employee(models.Model):
    name = models.CharField(max_length=50, default='')
    picture = CloudinaryField('image')
    email = models.CharField(max_length=50)
    description = models.TextField(default='')

    def __str__(self):
        return self.name
