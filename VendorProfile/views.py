from .models import VendorProfile
from rest_framework import generics, response, status
from .serializer import VendorProfileSerializer

# Create your views here.
class VendorProfileListCreate(generics.ListCreateAPIView):
    queryset = VendorProfile.objects.all()
    serializer_class = VendorProfileSerializer

    def post(self, request, *args, **kwargs):
        serializer = VendorProfileSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            data = dict(serializer.data)
            return response.Response({
                "message": "Vendor Profile Created Successfully",
                "vendor_name": data["vendor_name"],
                "vendor_code": data["vendor_code"],
                "contact_number": data["contact_number"],
                "address": data["address"],
            }, status=status.HTTP_201_CREATED)
        
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VendorProfileRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = VendorProfile.objects.all()
    serializer_class = VendorProfileSerializer