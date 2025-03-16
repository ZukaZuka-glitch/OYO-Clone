from django.shortcuts import render, redirect
import accounts.models as models
from django.contrib import messages
from django.db.models import Q
from .utils import generate_random_token

# Create your views here.
def login_page(r):
    return render(r, "login.html")

def register_page(r):
    if r.method == 'POST':
        first_name = r.POST.get('first_name')
        last_name = r.POST.get('last_name')
        email = r.POST.get('email')
        phone_number = r.POST.get('phone_number')
        pass1 = r.POST.get('password1')
        pass2 = r.POST.get('password2')
        if models.HotelUser.objects.filter(Q(email=email) | Q(phone_number=phone_number)).exists():
            messages.error(r, "Account exists with email or phone number.")
            return redirect(login_page)
        if pass1 == pass2:
            hotel_user = models.HotelUser.objects.create(first_name=first_name, last_name=last_name,
                                                 email=email, phone_number=phone_number,
                                                 email_token=generate_random_token(), username=phone_number)
            hotel_user.set_password(pass1)
            hotel_user.save()
            messages.success(r, "Account created successfully.")
            return redirect(login_page)
    return render(r, "register.html")
