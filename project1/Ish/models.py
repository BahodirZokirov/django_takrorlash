from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
class Qurilish (models.Model):
    salary = models.DecimalField(max_digits=11, decimal_places=2)
    location = models.CharField(max_length=50)
    position = models.CharField(max_length=25)
    description = models.TextField()


    def __str__(self):
        return self.position


class Restoran (models.Model):
    gender = models.CharField(max_length=10)
    limit_age = models.IntegerField(validators=(MinValueValidator(16), MaxValueValidator(28)))
    position = models.CharField(max_length=25)
    salary = models.DecimalField(max_digits=11, decimal_places=2)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.position


