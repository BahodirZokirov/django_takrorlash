from django.db import models

# Create your models here.


class BolalarKiyimlari (models.Model):
    size = models.PositiveSmallIntegerField()
    color = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(default='media/BolalarDunyosi/default_bolalar_kiyimlari.', upload_to='media/BolalarDunyosi')

    def __str__(self):
        return self.price


class BolalarOyinchoqlari (models.Model):
    name = models.CharField(max_length=25)
    color = models.CharField(max_length=25)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(default='media/BolalarDunyosi/default_bolalar_oyinchoqlari.', upload_to='media/BolalarDunyosi')

    def __str__(self):
        return self.name



