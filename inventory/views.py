from django.shortcuts import render, redirect
from .forms import ProductUploadForm
from .models import Product
from product_cart.models import ProductCart

# Create your views here.
def product_upload_view(request):
    if request.method == "POST":
        form = ProductUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("product_list_view")
    else:
        form = ProductUploadForm()
    return render(request, "inventory/product_upload.html", {"form":form})


def product_list(request):
    products = Product.objects.all()
    return render (request, "inventory/product_list.html", {"products": products})



def product_details(request, id):
    product = Product.objects.get(id = id)
    return render(request, "inventory/product_details.html", {"product": product})



def product_update_view(request, id):
    product = Product.objects.get(id=id)
    if request.method == "POST":
        form = ProductUploadForm(request.POST, request.FILES, instance= product)
        if form.is_valid():
            form.save()
            return redirect("product_list_view")
    else:
        form = ProductUploadForm(instance= product)
    return render(request, "inventory/edit_product.html", {"form": form})
        

def delete_product(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect("product_list_view")