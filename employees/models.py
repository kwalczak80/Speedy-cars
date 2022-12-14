from datetime import datetime
from django.db import models
from cloudinary.models import CloudinaryField


class Employee(models.Model):
    """
    The Employee model
    """
    name = models.CharField(max_length=100, default='')
    photo = CloudinaryField('image')
    description = models.TextField(default='')
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50, default='')
    hire_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        """
        Return the employee name
        """
        return self.name
