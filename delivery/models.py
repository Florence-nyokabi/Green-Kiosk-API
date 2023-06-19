from django.db import models
# from orders.models import Order

class Delivery(models.Model):
    order_name = models.CharField(max_length=32)
    contact_number = models.IntegerField()
    delivery_date = models.DateTimeField()
    delivery_time = models.TimeField()
    delivery_driver_name=models.CharField(max_length=32)
    delivery_address=models.CharField(max_length=32)
    delivery_status=models.CharField(max_length=32)
    # order = models.ForeignKey(Order, null=True, on_delete=models.CASCADE)

class Meta:
        verbose_name_plural = "delivery"