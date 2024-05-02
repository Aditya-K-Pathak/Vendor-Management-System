"""
This module defines API views for managing Vendor Profiles using Django REST Framework.

Endpoints:
- POST /api/vendors/: Create a new vendor profile.
- GET /api/vendors/: List all vendor profiles.
- GET /api/vendors/{vendor_id}/: Retrieve details of a specific vendor profile.
- PUT /api/vendors/{vendor_id}/: Update details of a specific vendor profile.
- DELETE /api/vendors/{vendor_id}/: Delete a specific vendor profile.
"""

from rest_framework import generics, response, status
from .models import VendorProfile
from .serializer import VendorProfileSerializer

class VendorProfileListCreate(generics.ListCreateAPIView):
    """
    API view for creating and listing vendor profiles.
    """
    queryset = VendorProfile.objects.all()
    serializer_class = VendorProfileSerializer

    def post(self, request, *args, **kwargs):
        """
        Create a new vendor profile.
        """
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
    """
    API view for retrieving, updating, and deleting a vendor profile.
    """
    queryset = VendorProfile.objects.all()
    serializer_class = VendorProfileSerializer

    def put(self, request, *args, **kwargs):
        """
        Update details of a specific vendor profile.
        """
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """
        Delete a specific vendor profile.
        """
        return self.destroy(request, *args, **kwargs)
