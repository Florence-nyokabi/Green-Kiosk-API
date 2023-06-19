from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField



# Create your models here.
class Customer(models.Model):
    first_name=models.CharField(max_length=32)
    last_name=models.CharField(max_length=32)
    email_address=models.EmailField(unique=True)
    phone_number = PhoneNumberField()
    home_address=models.CharField(max_length=32)
    order_history= models.JSONField()
    payment_method=models.CharField(max_length=32)
    rating = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)], default=0.0)
    user = models.OneToOneField(User, null= True, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to="customer_profiles/", blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
   



class Meta:
        verbose_name_plural = "customer"
        ordering = ["first_name", "last_name"]

