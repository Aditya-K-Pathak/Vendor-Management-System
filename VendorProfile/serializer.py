from rest_framework import serializers
from .models import VendorProfile

class VendorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorProfile
        fields = '__all__'
        
class VendorProfileSerializerPOST(serializers.ModelSerializer):
    class Meta:
        model = VendorProfile
        fields = ('vendor_code', 'vendor_name', 'contact_number', 'address')