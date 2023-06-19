from django.db import models
from inventory.models import Product

# Create your models here.
class ProductCart(models.Model):
    product_name = models.CharField(max_length=32)
    product_price = models.DecimalField(decimal_places=2, max_digits=10)
    product_quantity = models.IntegerField()
    product_image = models.ImageField()
    products = models.ManyToManyField(Product)
