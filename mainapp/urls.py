from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import *
urlpatterns = [
    path("SignupAndSignin/", loginAndSignup, name='SignupAndSignin'),
    path("", MainPage, name='MainPage'),
    path("contact/", Contact, name='contact'),
    path("contact1/", Contact1, name='contact1'),
    path("trackTickets/", TrackTickets, name='tracktickets'),
    path("admin_login/", AdminLogin, name='admin_login'),
    path("registration_view/", registration_view, name='registration_view'),
    path("login_view/", login_view, name='login_view'),
    path('logout/', logout_view, name='logout'),
    path('userHome/', UserHome, name='userHome'),
    path('home/', home, name='home'),
    path('book_tickets/', book_tickets, name='book_tickets'),
    path('confirm_booking/', confirm_booking, name='confirm_booking'),
    path('book_tickets/<int:bus_number>/', book_tickets, name='book_tickets'),


]
