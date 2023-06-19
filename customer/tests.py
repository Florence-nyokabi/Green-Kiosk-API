from django.test import TestCase
from django.contrib.auth.models import User
from customer.models import Customer
from django.core.exceptions import ValidationError

class CustomerModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password123")

    def test_create_customer(self):

        """Test successful creation of a Customer instance."""
        customer = Customer.objects.create(
            first_name="John",
            last_name="Doe",
            email_address="john.doe@example.com",
            phone_number="+123456789",
            home_address="123 Main St",
            order_history={"orders": []},
            payment_method="Credit Card",
            rating=4.5,
            user=self.user,
        )
        self.assertEqual(customer.first_name, "John")
        self.assertEqual(customer.email_address, "john.doe@example.com")
        self.assertEqual(customer.rating, 4.5)
        self.assertEqual(customer.user, self.user)

    def test_rating_validation(self):
        """Test that rating validation works."""
        with self.assertRaises(ValidationError):
            customer = Customer.objects.create(
                first_name="Test",
                last_name="Doe",
                email_address="test.doe@example.com",
                phone_number="+987654321",
                home_address="456 Elm St",
                order_history={"orders": []},
                payment_method="PayPal",
                rating=6.0,  # Invalid rating
                user=self.user,
            )
            customer.full_clean()


        """Test phone number validation using PhoneNumberField."""

    def test_phone_number_format(self):
        with self.assertRaises(ValidationError):
            customer = Customer(
                first_name="Invalid",
                last_name="Phone",
                email_address="invalid.phone@example.com",
                phone_number="invalid_number",  
                home_address="789 Oak St",
                order_history={"orders": []},
                payment_method="Cash",
                rating=4.0,
                user=self.user,
            )
            customer.full_clean()

    def test_email_uniqueness(self):
        """Test that email addresses must be unique."""
        Customer.objects.create(
            first_name="Alice",
            last_name="Test",
            email_address="flo@example.com",
            phone_number="+123456789",
            home_address="123 Pine St",
            order_history={"orders": []},
            payment_method="Credit Card",
            rating=4.0,
            user=self.user,
        )
        with self.assertRaises(Exception):
            Customer.objects.create(
                first_name="Flo",
                last_name="Test",
                email_address="flo@example.com",  # Duplicate email
                phone_number="+987654321",
                home_address="456 Test  St",
                order_history={"orders": []},
                payment_method="PayPal",
                rating=3.5,
                user=self.user,
            )

    def test_customer_string_representation(self):
        """Test the __str__ method of the Customer model."""
        customer = Customer.objects.create(
            first_name="Test",
            last_name="User",
            email_address="test.user@example.com",
            phone_number="+123456789",
            home_address="123 Test St",
            order_history={"orders": []},
            payment_method="Debit Card",
            rating=5.0,
            user=self.user,
        )
        self.assertEqual(str(customer), "Test User")

    def test_optional_profile_picture(self):
        """Test that profile picture is optional."""
        customer = Customer.objects.create(
            first_name="flo",
            last_name="User",
            email_address="flo@example.com",
            phone_number="+123456789",
            home_address="Home 123",
            order_history={"orders": []},
            payment_method="Cash",
            rating=3.0,
            user=self.user,
        )
        self.assertFalse(bool(customer.profile_picture))