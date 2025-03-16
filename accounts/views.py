from django.shortcuts import render, redirect
import accounts.models as models
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse
from .utils import generate_random_token, send_verification_mail
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def login_page(r):
    if r.method == 'POST':
        email = r.POST.get('email')
        password = r.POST.get('password')
        user_obj = models.HotelUser.objects.filter(email=email)
        if not user_obj.exists():
            messages.error(r, 'No Account Found!')
            return redirect(login_page)
        if not user_obj[0].is_verified:
            messages.error(r, 'Account Not Verified!')
            return redirect(login_page)
        hotel_user = authenticate(username=user_obj[0].username,password=password)
        if hotel_user:
            login(r, hotel_user)
            messages.success(r, 'Login Successful!')
            return redirect('/')
        messages.error(r, 'Login Failed!')
        return redirect(login_page)
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
            send_verification_mail(email, hotel_user.email_token)
            messages.success(r, "Account created successfully.")
            return redirect(login_page)
    return render(r, "register.html")

def verify_email_token(r, token):
    try:
        hotel_user = models.HotelUser.objects.get(email_token=token)
        hotel_user.is_verified = True
        hotel_user.save()
        messages.success(r, 'Account Verified Successfully!')
        return redirect(login_page)
    except models.HotelUser.DoesNotExist:
        return HttpResponse('<h2>Invalid token.</h2>')

def logout_page(r):
    logout(r)
    messages.success(r, 'Logout Successful!')
    return redirect('/')
