from rest_framework import routers
from .views import *
from django.urls import path, include

router = routers.SimpleRouter()
router.register(r'user', UserViewSet, basename='user')
router.register(r'review', ReviewViewSet, basename='review')

urlpatterns = [
    path('', include(router.urls)),
    path('property/', PropertyListAPIView.as_view(), name='property_list'),
    path('property/<int:pk>/', PropertyDetailAPIView.as_view(), name='property_detail'),
    path('booking/', BookingListAPIVIew.as_view(), name='booking_list'),
    path('booking/<int:pk>/', BookingDetailAPIVIew.as_view(), name='booking_detail'),
    # path('register/', RegisterView.as_view(), name='register'),
    # path('login/', CustomLoginView.as_view(), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout'),
]