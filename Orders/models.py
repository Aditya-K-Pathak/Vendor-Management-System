# Import necessary modules
import random
import datetime
from django.db import models
from django.utils import timezone
from VendorProfile.models import VendorProfile

def generate_random_po_number() -> int:
    """
    Generate a random 8-digit purchase order number.

    Returns:
        int: A randomly generated 8-digit purchase order number.
    """
    return random.randint(10000000, 99999999)

class Orders(models.Model):
    """
    Model to represent purchase orders.

    Attributes:
        po_number (models.BigAutoField): The unique identifier for the purchase order.
        vendor_code (models.ForeignKey): The vendor associated with the purchase order.
        order_status (models.CharField): The status of the purchase order.
        order_date (models.DateTimeField): The date and time when the order was placed.
        delivery_date (models.DateTimeField): The expected delivery date of the order.
        items (models.JSONField): The items included in the purchase order.
        quantity (models.IntegerField): The quantity of items in the purchase order.
        quality_rating (models.FloatField): The quality rating of the purchase order.
        issue_date (models.DateTimeField): The date and time when an issue occurred with the order.
        acknowledgement_date (models.DateTimeField): The date and time when the order was acknowledged.

    Methods:
        save(self, *args, **kwargs): Overrides the default save method to update vendor's new orders and orders received.
        __str__(self): Returns a string representation of the purchase order.
    """
    po_number = models.BigAutoField(default=generate_random_po_number, primary_key=True)
    vendor_code = models.ForeignKey(VendorProfile, on_delete=models.CASCADE)
    order_status = models.CharField(max_length=20, default='Pending')
    order_date = models.DateTimeField(default=timezone.now)
    delivery_date = models.DateTimeField(
        default=datetime.datetime.now() + datetime.timedelta(days=random.randint(1, 3))
    )
    items = models.JSONField(default={'Product_Name': 'Quantity'})
    quantity = models.IntegerField(default=0)
    quality_rating = models.FloatField(default=0)
    issue_date = models.DateTimeField(default=timezone.now)
    acknowledgement_date = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        """
        Overrides the default save method to update vendor's new orders and orders received.
        If the purchase order is not already in the vendor's new orders list, it updates
        the orders received count and adds the purchase order to the new orders list.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            None
        """
        if self.po_number not in self.vendor_code.new_orders:
            self.vendor_code.orders_received += 1
            self.vendor_code.new_orders.update({self.po_number: 'Pending'})
            self.vendor_code.save()

        super().save(*args, **kwargs)

    def __str__(self):
        """
        Returns a string representation of the purchase order.

        Returns:
            str: A string representing the purchase order.
        """
        return f"{self.po_number}-{self.vendor_code.vendor_name}"
