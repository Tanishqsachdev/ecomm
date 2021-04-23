from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Address(models.Model):
    building_number = models.CharField(max_length=20)
    street_name = models.CharField(max_length=20)
    locality = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    pincode = models.PositiveIntegerField(validators=[MinValueValidator(100000),MaxValueValidator(999999)])

    def __str__(self):
        return self.building_number
    