from django.shortcuts import render
from rest_framework.views import APIView
from customer.models import Customer
from inventory.models import Product
from orders.models import Order
from payment.models import Payment
from delivery.models import Delivery
from product_cart.models import ProductCart
from .serializers import CustomerSerializer, InventorySerializer, OrderSerializer, ProductCartSerializer
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class CustomerListView(APIView):
    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CustomerSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400)
    
class CustomerDetailView(APIView):
    def get(self, request, id, format=None):
        customer = Customer.objects.get(id=id)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)
    
    def put(self, request, id, format=None):
        customer = Customer.objects.get(id=id)
        serializer = CustomerSerializer(customer, request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
        return Response(serializer.errors, status = status.HTTP_400)
    
    def delete(self, request, id, format=None):
        customer = Customer.objects.get(id=id)
        customer.delete()
        return Response("Customer Deleted", status= status.HTTP_204_NO_CONTENT)



class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = InventorySerializer(products, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = InventorySerializer(data = request.data)
        if serializer.is_valid ():
            serializer.save()
            return  Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400)
    

class ProductDetailView(APIView):
    def get(self, request, id, format=None):
        product = Product.objects.get(id=id)
        serializer = ProductDetailView(product)
        return Response(serializer.data)
    
    def put(self, request, id, format=None):
        product = Product.objects.get(id=id)
        serializer = InventorySerializer(product, request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
        return Response(serializer.errors, status = status.HTTP_400)
    
    def delete(self, request, id, format=None):
        product = Product.objects.get(id=id)
        product.delete()
        return Response("Product Deleted", status= status.HTTP_204_NO_CONTENT)


class OrdersListView(APIView):
    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = OrderSerializer(data = request.data)
        if serializer.is_valid ():
            serializer.save()
            return  Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400)
    
class OrderDetailView(APIView):
    def get(self, request, id, format=None):
        order = Order.objects.get(id=id)
        serializer = OrderDetailView(order)
        return Response(serializer.data)
    
    def put(self, request, id, format=None):
        order = Order.objects.get(id=id)
        serializer = OrderSerializer(order, request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
        return Response(serializer.errors, status = status.HTTP_400)
    
    def delete(self, request, id, format=None):
        order = Order.objects.get(id=id)
        order.delete()
        return Response("Order Deleted", status= status.HTTP_204_NO_CONTENT)


class ProductCartListView(APIView):
    def get(self, request):
        product_cart = Order.objects.all()
        serializer = ProductCartSerializer(product_cart, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProductCartSerializer(data = request.data)
        if serializer.is_valid ():
            serializer.save()
            return  Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400)
    
class ProductCartDetailView(APIView):
    def get(self, request, id, format=None):
        product_cart = ProductCart.objects.get(id=id)
        serializer = ProductCartSerializer(product_cart)
        return Response(serializer.data)
    
    def put(self, request, id, format=None):
        order = Order.objects.get(id=id)
        serializer = ProductCartSerializer(order, request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
        return Response(serializer.errors, status = status.HTTP_400)
    
    def delete(self, request, id, format=None):
        product_cart= ProductCart.objects.get(id=id)
        product_cart.delete()
        return Response("Product cart deleted", status= status.HTTP_204_NO_CONTENT)
    
class AddToCartView(APIView):
    def post(self, request, format=None):
        cart_id = request.data["cart_id"]
        product_id = request.data["product_id"]
        cart = ProductCart.objects.get(id=cart_id)
        product = Product.objects.get(id=product_id)
        updated_cart = ProductCart.add_product(product)
        serializer = ProductCartSerializer(updated_cart)
        return Response(serializer.data)


class RemoveProductFromCartView(APIView):
    def post(self, request, format=None):
        cart_id = request.data.get("cart_id")
        product_id = request.data.get("product_id")
        try:
            cart = ProductCart.objects.get(id=cart_id)
            product = Product.objects.get(id=product_id)

            cart.products.remove(product)
            return Response("Product removed from cart successfully.", status=status.HTTP_200_OK)
        except ProductCart.DoesNotExist:
            return Response("Cart not found.", status=status.HTTP_404_NOT_FOUND)
        except Product.DoesNotExist:
            return Response("Product not found.", status=status.HTTP_404_NOT_FOUND)

class CheckoutView(APIView):
    def post(self, request, format=None):
        cart_id = request.data.get("cart_id")

        try:
            cart = ProductCart.objects.get(id=cart_id)
            order = Order.objects.create(customer=cart.customer, products=cart.products.all())
            cart.products.clear()
            return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)
        except ProductCart.DoesNotExist:
            return Response("Cart not found.", status=status.HTTP_404_NOT_FOUND)


class PaymentView(APIView):
    def post(self, request, format=None):
        order_id = request.data.get("order_id")
        payment_info = request.data.get("payment_info")

        try:
            order = Order.objects.get(id=order_id)
            payment = Payment.objects.create(order=order, payment_info=payment_info)
            return Response("Payment created and linked to the order successfully.", status=status.HTTP_201_CREATED)
        except Order.DoesNotExist:
            return Response("Order not found.", status=status.HTTP_404_NOT_FOUND)


class ShipmentView(APIView):
    def post(self, request, format=None):
        order_id = request.data.get("order_id")
        try:
            order = Order.objects.get(id=order_id)
            shipment = Delivery.objects.create(order=order)
            return Response("Shipment created successfully.", status=status.HTTP_201_CREATED)
        except Order.DoesNotExist:
            return Response("Order not found.", status=status.HTTP_404_NOT_FOUND)