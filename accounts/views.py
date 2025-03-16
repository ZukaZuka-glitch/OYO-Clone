from django.shortcuts import render
import accounts.models as models

# Create your views here.
def login_page(r):
    return render(r, "login.html")

def register_page(r):
    if r.method == 'POST':
        first_name = r.POST.get['first_name']
        last_name = r.POST.get['last_name']
        email = r.POST.get('email')
        pass1 = r.POST.get('password1')
        pass2 = r.POSt.get('password2')

    return render(r, "register.html")
