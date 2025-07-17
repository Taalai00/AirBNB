from rest_framework import serializers
from .models import *
import joblib
import os
from django.conf import settings

model_path = os.path.join(settings.BASE_DIR, 'model_nb.pkl')
model = joblib.load(model_path)

vec_path = os.path.join(settings.BASE_DIR, 'vec.pkl')
vec = joblib.load(vec_path)


class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'avatar']

class PropertyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'

class BookingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'property', 'guest', 'status', 'check_in', 'check_out', 'created_at']
        read_only_fields = ['id', 'guest', 'status', 'created_at']


class BookingUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'status', 'check_in', 'check_out']
        read_only_fields = ['id', 'check_in', 'check_out']


class ReviewSerializers(serializers.ModelSerializer):
    quest_user = UserProfileSerializers(read_only=True)
    check_comment = serializers.SerializerMethodField()
    class Meta:
        model = Review
        fields = ['rating', 'comment', 'created_at', 'check_comment', 'quest_user']

    def get_check_comment(self, obj):
        return model.predict(vec.transform([obj.comment]))

class PropertySerializers(serializers.ModelSerializer):
    owner = UserProfileSerializers()
    reviews = ReviewSerializers(many=True, read_only=True)
    class Meta:
        model = Property
        fields = [
            'id',
            'title',
            'description',
            'price_per_night',
            'city',
            'property_type',
            'rules',
            'max_guests',
            'owner',
            'images',
            'reviews'
        ]
    # def get_check_comment(self, obj):
    #     return model.predict(vec.transform([obj.comment]))