from django.db import models
from datetime import timedelta
from django.utils import timezone
from VendorProfile.models import VendorProfile

class Performance(models.Model):
    """
    This class represents the Performance model. It stores performance metrics for vendors.
    """

    vendor_code = models.ForeignKey(VendorProfile, primary_key=True, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    on_time_delivery_rate = models.FloatField(default=0)
    quality_rating_avg = models.FloatField(default=0)
    avg_response_time = models.DurationField(null=True, default=None)
    fulfilment_rate = models.FloatField(default=0)

    @classmethod
    def create_or_get(cls, vendor_code_id: int, on_time_delivery_rate: float, quality_rating_avg: float,
                      avg_response_time: timedelta, fulfilment_rate: float) -> "Performance":
        """
        Creates or retrieves a Performance object for the given vendor_code_id.

        Args:
            vendor_code_id (int): The ID of the VendorProfile object.
            on_time_delivery_rate (float): The on-time delivery rate for the given date.
            quality_rating_avg (float): The average quality rating for the given date.
            avg_response_time (timedelta): The average response time for the given date.
            fulfilment_rate (float): The fulfilment rate for the given date.

        Returns:
            Performance: The Performance object for the given vendor_code_id.
        """
        try:
            performance = cls.objects.get(vendor_code_id=vendor_code_id)
            performance.date = timezone.now()
            performance.on_time_delivery_rate = on_time_delivery_rate
            performance.quality_rating_avg = quality_rating_avg
            performance.avg_response_time = avg_response_time
            performance.fulfilment_rate = fulfilment_rate
        except cls.DoesNotExist:
            performance = cls(
                vendor_code_id=vendor_code_id,
                date=timezone.now(),
                on_time_delivery_rate=on_time_delivery_rate,
                quality_rating_avg=quality_rating_avg,
                avg_response_time=avg_response_time,
                fulfilment_rate=fulfilment_rate,
            )
            performance.save()
        return performance
