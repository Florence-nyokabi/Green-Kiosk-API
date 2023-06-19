# Green Kiosk

Green Kiosk is a Django-based e-commerce platform designed specifically for grocery shopping. It enables users to easily browse a wide selection of grocery products, add items to their carts, and efficiently manage their orders.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Florence-nyokabi/Green-Kiosk-API
   cd Green-Kiosk-API
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
To run the project, use the following command:
```bash
python manage.py runserver
```
You can access the application at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

# API Endpoints

## Product Endpoints
- **GET** `/api/products/`                - Retrieve a list of all products.
- **POST** `/api/products/`               - Create a new product.
- **GET** `/api/products/{id}/`           - Retrieve details of a specific product by ID.
- **PUT** `/api/products/{id}/`           - Update details of a specific product by ID.
- **DELETE** `/api/products/{id}/`        - Delete a specific product by ID.

## Customer Endpoints
- **GET** `/api/customers/`               - Retrieve a list of all customers.
- **POST** `/api/customers/`               - Create a new customer.
- **GET** `/api/customers/{id}/`          - Retrieve details of a specific customer by ID.
- **PUT** `/api/customers/{id}/`          - Update details of a specific customer by ID.
- **DELETE** `/api/customers/{id}/`       - Delete a specific customer by ID.

## Product Cart Endpoints
- **GET** `/api/cart/`                    - Retrieve a list of all product carts.
- **POST** `/api/cart/`                   - Create a new product cart.
- **GET** `/api/cart/{id}/`               - Retrieve details of a specific product cart by ID.
- **PUT** `/api/cart/{id}/`               - Update details of a specific product cart by ID.
- **DELETE** `/api/cart/{id}/`            - Delete a specific product cart by ID.

## Additional Cart Operations
- **POST** `/api/add_to_cart/`            - Add a product to a specific cart.
- **POST** `/api/remove_from_cart/`       - Remove a product from a specific cart.

## Order Endpoints
- **GET** `/api/orders/`                  - Retrieve a list of all orders.
- **POST** `/api/orders/`                 - Create a new order.
- **GET** `/api/orders/{id}/`             - Retrieve details of a specific order by ID.
- **PUT** `/api/orders/{id}/`             - Update details of a specific order by ID.
- **DELETE** `/api/orders/{id}/`          - Delete a specific order by ID.

## Checkout and Payment Endpoints
- **POST** `/api/checkout/`               - Create an order from the cart.
- **POST** `/api/payment/`                 - Process a payment for an order.
- **POST** `/api/shipment/`                - Create a shipment for an order.