from django.shortcuts import render

# Create your views here.
def index(r):
    return render(r, "index.html")

def login_page(r):
    return render(r, "login.html")

def register_page(r):
    return render(r, "register.html")
