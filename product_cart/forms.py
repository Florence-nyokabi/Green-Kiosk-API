from django import forms
from  .models import ProductCart

class ProductCartForm(forms.ModelForm):
    class Meta:
        model = ProductCart
        fields = "__all__"

