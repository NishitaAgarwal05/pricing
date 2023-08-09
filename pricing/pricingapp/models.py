from django.db import models
from  django.core.validators import MinValueValidator
# Create your models here.
DAYS_OF_WEEK = (
    ('0', 'Monday'),
    ('1', 'Tuesday'),
    ('2', 'Wednesday'),
    ('3', 'Thursday'),
    ('4', 'Friday'),
    ('5', 'Saturday'),
    ('6', 'Sunday'),
)

class DistanceBasePrice(models.Model):
    price = models.IntegerField(validators=[MinValueValidator(0)])
    distance = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0)])
    day = models.CharField(max_length = 1, choices=DAYS_OF_WEEK)
    class Meta:
        ordering  = ['id']

class DistanceAdditionalPrice(models.Model):
    price = models.IntegerField(validators=[MinValueValidator(0)])
    distance = models.DecimalField(max_digits=6,decimal_places=2, validators=[MinValueValidator(0)])

    class Meta:
        ordering  = ['id']

class TimeMultiplicationFactor(models.Model):
    time = models.TimeField()           # in hours
    multiplication_factor = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        ordering  = ['id']

class WaitingCharges(models.Model):
    buffer = models.TimeField()         #in minutes
    waiting_rate = models.IntegerField()
    waiting_time = models.TimeField()   #in minutes

    class Meta:
        ordering  = ['id']


