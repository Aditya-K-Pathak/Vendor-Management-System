import string
import random
import datetime
from django.utils import timezone
from django.db import models

def generate_vendor_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

# Create your models here.
class VendorProfile(models.Model):
    vendor_code = models.CharField(
        max_length=8, unique=True, primary_key=True, default=generate_vendor_code
    )
    vendor_name = models.CharField(max_length=100)
    contact_number = models.IntegerField(max_length=10, unique=True)
    address = models.TextField()
    new_orders = models.JSONField(default = {})
    orders_received = models.IntegerField(default=0)
    orders_fulfilled = models.IntegerField(default=0)
    fulfillment_rate = models.FloatField(default = 0)
    on_time_delivery = models.IntegerField(default=0)
    on_time_delivery_rate = models.FloatField(default=0)
    quality_rating_avg = models.FloatField(default=0)
    avg_response_time = models.DurationField(null = True, default=None)
    total_rating = models.IntegerField(default=0)
    ratings_given = models.IntegerField(default=0)
    orders_cancelled = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        from Performance.models import Performance
        
        def update_order_status(self, *args, **kwargs):
            ...

        performance, _ = Performance.objects.get_or_create(
            vendor_code=self.vendor_code,
            on_time_delivery_rate = self.on_time_delivery_rate,
            quality_rating_avg = self.quality_rating_avg,
            avg_response_time = self.avg_response_time,
            fulfilment_rate = self.fulfillment_rate,
        )
        performance.save()
        
        for po_number, status in self.new_orders.items():
            from Orders.models import Orders
            try:
                order = Orders.objects.get(po_number=po_number)
            except:
                ...

            if (status == 'Completed' or status == 'Declined') and order.order_status == 'Pending':

                if status == 'Completed':
                    order.order_status = 'Completed'
                    self.orders_fulfilled += 1
                    self.fulfillment_rate = self.orders_fulfilled / (self.orders_received)

                    if order.delivery_date - timezone.now() > datetime.timedelta(0):
                        self.on_time_delivery += 1
                    self.on_time_delivery_rate = self.on_time_delivery / self.orders_fulfilled
                    if order.quality_rating > 0:
                        self.total_rating += order.quality_rating
                        self.ratings_given += 1
                        self.quality_rating_avg = self.total_rating / self.ratings_given
                else:
                    order.order_status = 'Declined'
                    self.orders_cancelled += 1

                if self.avg_response_time:self.avg_response_time = ((self.avg_response_time * (self.orders_received - 1)) + (timezone.now() - order.order_date))/self.orders_received
                else:self.avg_response_time = timezone.now() - order.order_date
                
                order.save()

        super().save(*args, **kwargs)

    def __str__(self):
        return self.vendor_code + ' | ' + self.vendor_name 