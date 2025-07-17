from .serializers import *
from .models import *
from rest_framework import viewsets, generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .filters import PropertyFilter
from rest_framework.filters import SearchFilter, OrderingFilter
# from .paginations import LargeResultsSetPagination
from rest_framework import status
from .permissions import CheckOwner, CheckStoreOwner, CheckUserReview

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializers

class PropertyListAPIView(generics.ListAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializers
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = PropertyFilter
    search_fields = ['title']
    ordering_fields = ['price_per_night']

class PropertyDetailAPIView(generics.RetrieveAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializers

class PropertyListOwnerAPIView(generics.ListAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializers

    def get_queryset(self):
        return Property.objects.filter(owner=self.request.user)


class PropertyCreateAPIView(generics.CreateAPIView):
    serializer_class = PropertyCreateSerializer
    permission_classes = [CheckOwner]

class PropertyDetailUpdateDestroyOwnerAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertyCreateSerializer
    permission_classes = [CheckOwner, CheckStoreOwner]

class BookingListAPIVIew(generics.ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializers

class BookingDetailAPIVIew(generics.RetrieveAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializers

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers