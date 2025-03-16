from uuid import uuid4
from django.conf import settings
from django.core.mail import send_mail

def generate_random_token(): return str(uuid4())

def send_verification_mail(email, token):
    subject = 'Verify your email address'
    message = F"""Hi, please verify your email address by clicking on this link:
            127.0.0.1:8000/accounts/verify-account/{token}"""
    send_mail(subject, message, settings.EMAIL_HOST_USER, [email], fail_silently=False)