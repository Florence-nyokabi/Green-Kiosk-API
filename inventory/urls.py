from django.urls import path
from .views import product_upload_view, product_list, product_details, product_update_view, delete_product

urlpatterns = [
    path("products/upload/", product_upload_view, name="product_upload_view"),
    path("products/list/", product_list, name="product_list_view"),
    path("products/<int:id>/", product_details, name="product_detail_view"),
    path("products/edit/<int:id>/", product_update_view, name = "product_update"),
    path("products/delete/<int:id>/", delete_product, name= "delete_product_view" ),
]
