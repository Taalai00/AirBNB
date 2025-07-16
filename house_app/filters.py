from django_filters import FilterSet
from .models import *

class PropertyFilter(FilterSet):
    class Meta:
        model = Property
        fields = {
            'country':['exact'],
            'year': ['gt', 'lt'],
            'genre': ['exact'],
            'status_movie': ['exact'],
            'actor': ['exact'],
            'director': ['exact'],
        }