from .models import Orders
from rest_framework import generics, response, status
from rest_framework.permissions import IsAuthenticated
from .serializer import OrdersSerializer

class OrdersListCreate(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    """
    API view for listing and creating orders.

    get:
    List all orders.

    post:
    Create a new order.
    """
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests to create a new order.

        :param request: HTTP request object containing data for creating the order.
        :return: HTTP response with created order data or error messages.
        """
        serializer = OrdersSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class OrdersRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    """
    API view for retrieving, updating, and deleting orders.

    get:
    Retrieve details of a specific order.

    put:
    Update a specific order.

    delete:
    Delete a specific order.
    """
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer

    def put(self, request, *args, **kwargs):
        """
        Handle PUT requests to update a specific order.

        :param request: HTTP request object containing data for updating the order.
        :return: HTTP response with updated order data or error messages.
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        """
        Handle DELETE requests to delete a specific order.

        :param request: HTTP request object.
        :return: HTTP response indicating successful deletion or error.
        """
        instance = self.get_object()
        instance.delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)
