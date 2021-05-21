from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.
DEFAULT_ID =1

class Address(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=DEFAULT_ID)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = models.PositiveBigIntegerField(validators=[MinValueValidator(1000000000)])
    building_number = models.CharField(max_length=20)
    street_name = models.CharField(max_length=20)
    locality = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    pincode = models.PositiveIntegerField(validators=[MinValueValidator(100000),MaxValueValidator(999999)])

    def __str__(self):
        return self.building_number

class ProductCategory(models.Model):
    name = models.CharField(max_length=100)
    code = models.IntegerField()
    description = models.CharField(max_length=100)
    parent_code = models.IntegerField()

class Product(models.Model):
    product_category = models.ForeignKey(ProductCategory,on_delete=models.SET_NULL,null=True)
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

class OrderItem(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    quantity = models.IntegerField(default=1)

    def item_total(self):
        return self.item.product_price * self.quantity

class Order(models.Model):
    user  = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    items = models.ManyToManyField(OrderItem)
    order_placed = models.DateTimeField(null=True,blank=True)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} ordered {[i.item.product_name for i in self.items.all()]}"
    
    def get_total(self):
        total = 0
        for item in self.items.all():
            total+= item.item_total()
        return total
    
