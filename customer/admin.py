from django.contrib import admin
from .models import Customer

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email_address", "home_address", "payment_method", "order_history", "rating", "user", "phone_number", "profile_picture")

admin.site.register(Customer, CustomerAdmin)    
