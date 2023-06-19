from django.shortcuts import render, redirect
from .models import ProductCart
from .models import Product
from .forms import ProductCartForm


def add_to_cart(request, id):
    product = Product.objects.get(id=id)

    cart_item = ProductCart (
        product_name = product.name,
        product_quantity = 1,
        product_price = product.price
    )

    cart_item.save()
    return redirect("product_list_view")


def view_cart(request):
    product_cart = ProductCart.objects.all()
    
    total_cart_price = 0

    for item in product_cart:
        item.total_price = item.product_price * item.product_quantity
        total_cart_price += item.total_price
    return render(request, "product_cart/view_cart.html", {"product_cart": product_cart, "total_cart_price": total_cart_price})




def remove_item(request, id):
    cart_item = ProductCart.objects.get(id=id)
    cart_item.delete()

    return redirect('view_cart')


def empty_cart(request):
    ProductCart.objects.all().delete()
    return redirect("view_cart")