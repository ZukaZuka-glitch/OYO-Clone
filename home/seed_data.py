from accounts.models import Amenities, HotelVendor, Hotel
from faker import Faker
from random import choice
fake = Faker()
import random

def create_user(num):
    for i in range(num):
        email = fake.unique.email()
        HotelVendor.objects.create(
            email = email,
            business_name = fake.name(),
            username = email,
            first_name = fake.name(),
            phone_number = random.randint(1111111111, 9999999999)
        )


def create_hotel(num):
    for i in range(num):
        hotel_vendor = choice(HotelVendor.objects.all())
        amenities = list(Amenities.objects.all())
        hotel = Hotel.objects.create(
            name=fake.company(),
            description=fake.text(),
            hotel_slug=fake.unique.slug(),
            hotel_owner=hotel_vendor,
            hotel_price=fake.random_number(digits=4) / 100.0,
            hotel_offer_price=fake.random_number(digits=4) / 100.0,
            hotel_location=fake.address(),
            is_active=fake.boolean()
        )
        hotel.amenities.set(amenities)