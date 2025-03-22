from django.shortcuts import render
from accounts.models import Hotel

# Create your views here.
def index(r):
    hotels = Hotel.objects.all()
    if r.GET.get('search'): hotels = hotels.filter(name__icontains=r.GET.get('search'))
    if r.GET.get('sort'):
        sort_by = r.GET.get('sort')
        if sort_by == 'sort_low': hotels = hotels.order_by('hotel_offer_price')
        else: hotels = hotels.order_by('-hotel_offer_price')
    return render(r, "index.html", context={"hotels": hotels[:50]})

def detail_hotel(r, slug):
    return render(r, "details.html", context={"hotel": Hotel.objects.get(hotel_slug=slug)})
