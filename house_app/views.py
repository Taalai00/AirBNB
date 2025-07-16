from .models import *
from .serializers import *
from rest_framework import viewsets, generics

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializers

class PropertyListAPIView(generics.ListAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializers

class PropertyDetailAPIView(generics.RetrieveAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializers

class BookingListAPIVIew(generics.ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializers

class BookingDetailAPIVIew(generics.RetrieveAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializers

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers