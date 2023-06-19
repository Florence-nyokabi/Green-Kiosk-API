from django.urls import path
from .views import display_vendors, remove_vendor, add_vendor


urlpatterns =[
    path('vendors/display/', display_vendors, name="display_vendors"),
    path('vendors/remove/<int:id>/', remove_vendor, name="remove_vendor"),
    path('vendors/add_vendor/', add_vendor, name="add_vendor")
]