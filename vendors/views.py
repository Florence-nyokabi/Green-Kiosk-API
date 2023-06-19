from django.shortcuts import redirect, render
from .forms import VendorForms
from .models import Vendors

# Create your views here.
def display_vendors(request):
    vendors = Vendors.objects.all()
    return render(request, 'vendors/display_vendors.html', {'vendors': vendors})

def remove_vendor(request, id):
    vendors = Vendors.objects.get(id=id)
    vendors.delete()
    return redirect("display_vendors")

def add_vendor(request):
    if request.method == "POST":
        form = VendorForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("display_vendors")
    else:
        form = VendorForms()
    return render(request, "vendors/add_vendor.html", {"form":form})