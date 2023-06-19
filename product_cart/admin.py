from django.contrib import admin
from .models import ProductCart

# Register your models here.
class Product_cartAdmin(admin.ModelAdmin):
    list_display=("product_name", "product_price", "product_quantity", "product_image")

admin.site.register(ProductCart, Product_cartAdmin)