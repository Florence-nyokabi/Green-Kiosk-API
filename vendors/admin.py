from django.contrib import admin
from .models import Vendors
# Register your models here.


class Vendors_Admin(admin.ModelAdmin):
    list_display = ("vendor_id" ,"vendor_name","vendor_email", "vendor_address", "vendor_ratings")

admin.site.register(Vendors, Vendors_Admin)
