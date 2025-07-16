from rest_framework import serializers
from .models import *

class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class PropertySerializers(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ['title', 'description', 'price_per_night', 'city', 'address', 'property_type', 'rules', 'max_guests', 'bedrooms', 'bathrooms', 'owner', 'images', 'is_active']

class BookingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['property', 'guest', 'check_in', 'check_out', 'status', 'created_at']

class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'