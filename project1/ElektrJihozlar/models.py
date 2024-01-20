from django.db import models

# Create your models here.
class Telefon (models.Model):
    name = models.CharField(max_length=25)
    make = models.CharField(max_length=25)
    color = models.CharField(max_length=25)
    SD = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(default='media/ElektrJihozlar/default_elektr_jihozlari.', upload_to='media/ElektrJihozlar')

    def __str__(self):
        return self.name


class Laptop (models.Model):
    name = models.CharField(max_length=25)
    make = models.CharField(max_length=25)
    color = models.CharField(max_length=25)
    price = models.PositiveIntegerField()
    image = models.ImageField(default='media/ElektrJihozlar/default_laptop', upload_to='media/ElektrJihozlar')

    def __str__(self):
        return self.name
