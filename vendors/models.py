from django.db import models

# Create your models here.

class Vendors(models.Model):
    vendor_id = models.IntegerField()
    vendor_image = models.ImageField(upload_to='media/', default='/')
    vendor_name = models.CharField(max_length=32)
    vendor_email = models.CharField(max_length=32)
    vendor_address = models.CharField(max_length=32)
    vendor_ratings = models.CharField(max_length=32)

class Meta:
    verbose_name_plural = "vendors"
