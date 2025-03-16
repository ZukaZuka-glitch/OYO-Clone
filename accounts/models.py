from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class HotelUser(User):
    profile_picture = models.ImageField(upload_to="profile_pictures", null=True, blank=True)
    phone_number = models.CharField(max_length=10, unique=True)
    email_token = models.CharField(max_length=100, null=True, blank=True)
    otp = models.CharField(max_length=10, null=True, blank=True)
    is_verified = models.BooleanField(default=False)


class HotelVendor(User):
    phone_number = models.CharField(max_length=10, unique=True)
    profile_picture = models.ImageField(upload_to="profile_pictures", null=True, blank=True)
    email_token = models.CharField(max_length=100, null=True, blank=True)
    otp = models.CharField(max_length=10, null=True, blank=True)
    is_verified = models.BooleanField(default=False)


class Amenities(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to="icons", null=True, blank=True)


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    hotel_slug = models.SlugField(max_length=100, unique=True)
    hotel_owner = models.ForeignKey(HotelVendor, on_delete=models.CASCADE, related_name='hotels')
    amenities = models.ManyToManyField(Amenities)
    hotel_price = models.FloatField()
    hotel_offer_price = models.FloatField()
    hotel_location = models.TextField()
    is_active = models.BooleanField(default=True)


class HotelImages(models.Model):
    hotel_owner = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to="hotel_images", null=True, blank=True)


class HotelManager(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='managers')
    manager_name = models.CharField(max_length=100)
    manager_contact = models.CharField(max_length=10)
