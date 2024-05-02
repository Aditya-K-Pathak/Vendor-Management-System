from.models import Performance
from.serializer import PerformanceSerializer
from rest_framework import generics

class PerformanceList(generics.ListAPIView):
    """
    This class represents a list view for Performance objects.

    Attributes:
    queryset : QuerySet
        A queryset of all Performance objects.
    serializer_class : PerformanceSerializer
        The serializer class to be used for serializing the Performance objects.
    """

    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer
