from django.db import models

# Create your models here.
class It (models.Model):
    name = models.CharField(max_length=25)
    color = models.CharField(max_length=25)
    image = models.ImageField(default='media/Hayvonlar/default_it.', upload_to='media/Hayvonlar')
    price = models.PositiveIntegerField()
    race = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Mushuk (models.Model):
    name = models.CharField(max_length=25)
    color = models.CharField(max_length=25)
    race = models.CharField(max_length=25)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(default="media/Hayvonlar/default_mushuk", upload_to="media/Hayvonlar")

    def __str__(self):
        return self.name
