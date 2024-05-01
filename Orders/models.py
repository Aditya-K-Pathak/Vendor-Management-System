import datetime
import random
from django.db import models
from django.utils import timezone
from VendorProfile.models import VendorProfile

def generate_random_po_number() -> int:
    return random.randint(10000000, 99999999)

# Create your models here.
class Orders(models.Model):
    po_number = models.BigAutoField(default = generate_random_po_number, primary_key=True)
    vendor_code = models.ForeignKey(VendorProfile, on_delete=models.CASCADE)
    order_status = models.CharField(max_length=20, default = 'Pending')
    order_date = models.DateTimeField(default=timezone.now())
    delivery_date = models.DateTimeField(
        default=datetime.datetime.now() + datetime.timedelta(days = random.randint(1, 3))
    )
    items = models.JSONField(default = {
        'Product_Name': 'Quantity',
    })
    quantity = models.IntegerField(default = 0)
    quality_rating = models.FloatField(default=0)
    issue_date = models.DateTimeField(default=timezone.now())
    acknowledgement_date = models.DateTimeField(default=timezone.now())

    def save(self, *args, **kwargs):
        # update if there is a new order
        def update_received_orders(self, *args, **kwargs):
            self.vendor_code.orders_received += 1
            self.vendor_code.new_orders.update({
                self.po_number: 'Pending'
            })

        def update_fulfilment_rate(self, *args, **kwargs):
            try:
                self.vendor_code.fulfilment_rate = (
                    self.vendor_code.order_fulfilled / self.vendor_code.orders_received
                )
            except ZeroDivisionError:
                self.vendor_code.fulfilment_rate = 0

        if self.po_number not in self.vendor_code.new_orders:
            update_received_orders(self, *args, **kwargs)
            self.vendor_code.save()
        # else:
        #     if self.quality_rating > 0 and self.order_status == 'Completed':
        #         self.vendor_code.total_rating += self.quality_rating

        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.po_number) + '-' + self.vendor_code.vendor_name
