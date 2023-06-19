from django import forms
from .models import Vendors

class VendorForms(forms.ModelForm):
    vendor_id = forms.IntegerField()
    vendor_name = forms.CharField(max_length=32)
    vendor_image = forms.ImageField()
    vendor_email = forms.CharField(max_length=32)
    vendor_address = forms.CharField(max_length=32)
    vendor_ratings = forms.CharField(max_length=32)

    class Meta:
        model = Vendors
        fields = "__all__"
