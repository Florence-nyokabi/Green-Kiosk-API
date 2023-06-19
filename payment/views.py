from django.shortcuts import render, redirect
from product_cart.models import ProductCart
from .models import Payment
from .forms import PaymentForm
from datetime import datetime


def make_payment(request):
    product_cart = ProductCart.objects.all()

    

    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            product_cart.delete()
            return redirect('')
    else:
        form = PaymentForm()

    return render(request, 'payment/make_payment.html', {'form': form})