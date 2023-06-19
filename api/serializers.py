from rest_framework import serializers

from customer.models import Customer
from product_cart.models import ProductCart
from inventory.models import Product
from orders.models import Order
from delivery.models import Delivery


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"

class ProductCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCart
        fields = "__all__"

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

    
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"