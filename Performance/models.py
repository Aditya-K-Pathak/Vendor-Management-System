from django.db import models
from django.utils import timezone
from VendorProfile.models import VendorProfile

# Create your models here.
class Performance(models.Model):
    vendor_code = models.ForeignKey(VendorProfile, primary_key = True, on_delete = models.CASCADE)
    date = models.DateField(auto_now_add=True)
    on_time_delivery_rate = models.FloatField(default=0)
    quality_rating_avg = models.FloatField(default=0)
    avg_response_time = models.DurationField(null = True, default=None)
    fulfilment_rate = models.FloatField(default=0)

    @classmethod
    def create_or_get(cls, vendor_code_id, on_time_delivery_rate, quality_rating_avg,
            avg_response_time,
            fulfilment_rate):
        try:
            # Try to get the Performance object for the given vendor_code_id
            performance = cls.objects.get(vendor_code_id=vendor_code_id)
            performance.date = timezone.now()
            performance.on_time_delivery_rate = on_time_delivery_rate
            performance.quality_rating_avg = quality_rating_avg
            performance.avg_response_time = avg_response_time
            performance.fulfilment_rate = fulfilment_rate
        except cls.DoesNotExist:
            # If the object does not exist, create a new one
            performance = cls(
                vendor_code_id=vendor_code_id, 
                date = timezone.now(),
                on_time_delivery_rate = on_time_delivery_rate,
                quality_rating_avg = quality_rating_avg,
                avg_response_time = avg_response_time,
                fulfilment_rate = fulfilment_rate,
            )
            performance.save()
        return performance
    