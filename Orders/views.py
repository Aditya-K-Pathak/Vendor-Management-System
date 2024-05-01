from .models import Orders
from rest_framework import generics, response, status
from .serializer import OrdersSerializer

class OrdersListCreate(generics.ListCreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer

    def post(self, request, *args, **kwargs):
        serializer = OrdersSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class OrdersRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer