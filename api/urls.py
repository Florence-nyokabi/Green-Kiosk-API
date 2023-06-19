from django.urls import path
from .views import CustomerListView, CustomerDetailView, ProductListView, ProductDetailView, OrdersListView,OrderDetailView, ProductCartListView, ProductCartDetailView,AddToCartView, RemoveProductFromCartView, ShipmentView, PaymentView,CheckoutView

urlpatterns = [
    path("customers/", CustomerListView.as_view(), name="customer_list_view"),
    path("customers/<int:id>/", CustomerDetailView.as_view(), name="customer_detail_view"),
    path("inventory/", ProductListView.as_view(), name="product_list_view"),
    path("inventory/<int:id>/", ProductDetailView.as_view(), name="product_detail_view"),
    path("orders/", OrdersListView.as_view(), name="order_list_view"),
    path("orders/<int:id>/",OrderDetailView.as_view(), name="order_detail_view" ),
    path("product_cart/", ProductCartListView.as_view(), name="product_cart_list_view"),
    path("product_cart/<int:id>/", ProductCartDetailView.as_view(), name="product_cart_detail_view"),
    # path("add_to_cart/", AddToCartView.as_view(), name="add_to_cart" ),
    # path("remove_from_cart/", RemoveProductFromCartView.as_view(), name="remove_from_cart"),
    path("checkout/", CheckoutView.as_view(), name="checkout"),
    path("payment/", PaymentView.as_view(), name="Payment"),
    path("ship/", ShipmentView.as_view(), name= "shipment"),
]