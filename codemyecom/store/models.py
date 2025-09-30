from django.db import models
import datetime

# Create your models here.

class Catagory(models.Model):
    name = models.CharField(max_length=145)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'catagories'
    
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.first_name}{self.last_name}'
        
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=250, default='', blank=True)
    image = models.ImageField(upload_to='static')

    # is on sale or not
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=150, default='', blank=True)
    phone = models.CharField(max_length=20, default='', blank=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.product