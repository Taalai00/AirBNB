from django.contrib import admin
from .models import *

admin.site.register(UserProfile)
admin.site.register(Property)
admin.site.register(Booking)
admin.site.register(Review)