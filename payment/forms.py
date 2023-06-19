from django import forms
from .models import Payment

class PaymentForm(forms.ModelForm):
    payment_method = forms.CharField(max_length=32, label='Payment Method')
    currency = forms.CharField(max_length=4, label='Currency')
    
    class Meta:
        model = Payment
        fields = "__all__"