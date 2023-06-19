from django.db import models
from vendors.models import Vendors

# Create your models here.
class Product(models.Model):

    name=models.CharField(max_length=32)
    price=models.DecimalField(max_digits=8, decimal_places=2)
    description=models.TextField()
    image=models.ImageField()
    image = models.ImageField(upload_to='media/images')
    date_created=models.DateTimeField(auto_now_add=True)
    stock=models.PositiveIntegerField() 
    vendor = models.ForeignKey(Vendors, null=True, on_delete = models.CASCADE)


    def add_product(self, product):
        self.products.add(product)
        self.save()
        return self
    
    def get_total(self):
        products = self.products.all()
        total = 0
        for product in products:
            total += product.price
        return total
    # total = sum([product.price for product in self.products.all()])

class Meta:
        verbose_name_plural = "product"
