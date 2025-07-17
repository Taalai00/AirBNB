from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Model


class UserProfile(AbstractUser):
    phone_number = models.CharField(max_length=20, blank=True)
    avatar = models.ImageField(upload_to='profiles/', blank=True, null=True)
    role = [
        ('guest', 'guest'),
        ('host', 'host'),
    ]
    role_choices = models.CharField(max_length=10, choices=role)

class Property(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    city = models.CharField(max_length=32)
    address = models.CharField(max_length=64)
    PROPERTY_TYPE = [
        ('apartment', 'apartment'),
        ('house', 'house'),
        ('studio', 'studio')
    ]
    property_type = models.CharField(max_length=10, choices=PROPERTY_TYPE)
    RULE_CHOICES = [
        ('no_smoking', 'no_smoking'),
        ('pets_allowed', 'pets_allowed'),
        ('etc', 'etc')
    ]
    rules = models.CharField(max_length=12, choices=RULE_CHOICES)
    max_guests = models.PositiveSmallIntegerField()
    bedrooms = models.PositiveSmallIntegerField()
    bathrooms = models.PositiveSmallIntegerField()
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='properties')
    images = models.ImageField(upload_to='images_property/')
    is_active = models.BooleanField()

    def __str__(self):
        return self.title

class Booking(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    guest = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    check_in = models.DateTimeField(auto_now_add=True)
    check_out = models.DateTimeField(auto_now = True)
    STATUS_CHOICES = [
        ('pending', 'pending'),
        ('approved', 'approved'),
        ('rejected', 'rejected'),
        ('cancelled', 'cancelled')
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    created_at = models.DateField(auto_now=True)
    def __str__(self):
        return self.property

class Review(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='reviews')
    guest = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='quest_user')
    rating = models.IntegerField(choices=[(i, str(i))for i in range(1, 6)], null=True, blank=True)
    comment = models.TextField()
    created_at = models.DateField(auto_now=True)