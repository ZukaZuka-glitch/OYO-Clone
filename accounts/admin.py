from django.contrib import admin
from .models import HotelUser, HotelVendor, Amenities

# Register your models here.

admin.site.register(HotelUser)
admin.site.register(HotelVendor)
admin.site.register(Amenities)
