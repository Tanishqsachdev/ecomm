from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.
DEFAULT_ID =1

class Address(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=DEFAULT_ID)
    building_number = models.CharField(max_length=20)
    street_name = models.CharField(max_length=20)
    locality = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    pincode = models.PositiveIntegerField(validators=[MinValueValidator(100000),MaxValueValidator(999999)])

    def __str__(self):
        return self.building_number

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_description = models.CharField(max_length=150)
    product_image = models.ImageField(upload_to='static/products')
    product_price = models.FloatField()
    product_size = models.CharField(max_length=30)
    product_colors = models.CharField(max_length=20)
    units_in_stock = models.IntegerField()
    units_in_order = models.IntegerField()
    product_available = models.BooleanField(default=True)
    date_added = models.DateField(auto_now_add=True)