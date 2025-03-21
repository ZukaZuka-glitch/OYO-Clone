from django.shortcuts import render
from accounts.models import Hotel

# Create your views here.
def index(r):
    return render(r, "index.html", context={"hotels": Hotel.objects.all()[:50]})
