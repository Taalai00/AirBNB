from django_filters import FilterSet
from .models import *

class PropertyFilter(FilterSet):
    class Meta:
        model = Property
        fields = {
            'city':['exact'],
            'price_per_night': ['gt', 'lt'],
            'address': ['exact'],
            'property_type': ['exact'],
            'rules': ['exact'],
        }