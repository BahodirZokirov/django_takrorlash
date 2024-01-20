from django.db import models

# Create your models here.
class Car (models.Model):
    name = models.CharField(max_length=25)
    make = models.CharField(max_length=25)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    image = models.ImageField(upload_to='media/Transport')
    places = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name

class Plane (models.Model):
    name = models.CharField(max_length=25)
    make = models.CharField(max_length=25)
    image = models.ImageField(default='media/Transport/default_transport', upload_to='media/Transport')
    places = models.PositiveIntegerField()
    comfort = models.CharField(max_length=25)

    def __str__(self):
        return self.name