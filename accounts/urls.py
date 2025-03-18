"""
URL configuration for oyo_clone project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
import accounts.views as views

urlpatterns = [
    path('user-login/', views.user_login_page, name='user-login'),
    path('logout/', views.logout_page, name='logout'),
    path('user-register/', views.user_register_page, name='user-register'),
    path('verify-account/<str:token>', views.verify_email_token, name='verify'),
    path('send-otp/<str:email>/', views.send_otp, name='send_otp'),
    path('<str:email>/verify-otp', views.verify_otp, name='send_otp'),
    path('resend-otp/<str:email>', views.resend_otp, name='send_otp')
]
