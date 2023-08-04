from django.db import models

# Create your models here.
class DistanceBasePrice(models.Model):
    price = models.IntegerField()
    distance = models.DecimalField(max_digits=6, decimal_places=2)
    day = models.DateField()
    enable = models.BooleanField()

class DistanceAdditionalPrice(models.Model):
    price = models.IntegerField()
    distance = models.DecimalField(max_digits=6,decimal_places=2)
    enable = models.BooleanField()

