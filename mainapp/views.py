from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from .models import *
from django.contrib.auth import logout
import requests

from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render
def loginAndSignup(request):
    user = request.user  # Assuming you are using Django's authentication system
    return render(request, 'LoginAndSignup.html')

def MainPage(request):
    return render(request, "main.html")

def Contact(request):
    return render(request, "contact.html")
def Contact1(request):
    return render(request, "contact1.html")

def TrackTickets(request):
    return render(request, "Track_Tickets.html")

def UserHome(request):
    return render(request,template_name="userhome.html")

def AdminLogin(request):
    return render(request, "AdminLogin.html")


from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def registration_view(request):
    user_exists = False
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password1')  # Use 'password1' instead of 'password'
        name = request.POST.get('name')

        if User.objects.filter(email=email).exists():
            messages.info(request, 'User with this email already exists. Please log in.')
            return render(request, 'LoginAndSignup.html')

        user = User.objects.create_user(username=name, email=email, password=password, first_name=name)
        user.save()

        messages.info(request, 'Account created Successfully!')
        return render(request, 'LoginAndSignup.html')

    return render(request, 'LoginAndSignup.html')



def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')  # Use 'email' instead of 'username'
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                # If username and password match, redirect to the main page
                return render(request, 'userhome.html')
            else:
                # If password does not match, display a message
                messages.info(request, 'Invalid password. Please try again')
                return render(request, 'LoginAndSignup.html')

        except User.DoesNotExist:
            # If the user does not exist, display a message
            messages.info(request, 'User with this email does not exist')
            return render(request, 'LoginAndSignup.html')

    return render(request, 'LoginAndSignup.html')

def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return redirect('MainPage')



# views.py

# views.py

from django.shortcuts import render
from adminapp.models import BusRoute
from .forms import BusSearchForm

from django.shortcuts import render
from django.contrib import messages
from adminapp.models import BusRoute

def home(request):
    if request.method == 'POST':
        # Handle form submission and retrieve available buses
        from_location = request.POST.get('from_location')
        to_location = request.POST.get('to_location')
        date = request.POST.get('date')

        # Check if "From" and "To" are the same
        if from_location == to_location:
            messages.error(request, 'From and To locations cannot be the same.')
            return render(request, 'userhome.html')

        # Perform a query to get available buses based on the form inputs
        available_buses = BusRoute.objects.filter(source=from_location, destination=to_location, date=date)

        return render(request, 'userhome.html', {'available_buses': available_buses})

    # Render the initial page without the "No scheduled buses" message
    return render(request, 'userhome.html')


# In your_app/views.py

# views.py

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Bus, Booking


# views.py

from django.shortcuts import render, redirect
from django.contrib import messages
import random
from .models import Bus, Booking

# views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Bus, Booking
import random

def book_tickets(request, bus_number):
    bus = get_object_or_404(Bus, bus_number=bus_number)

    if request.method == 'POST':
        # Assuming the user is authenticated (you might want to handle authentication)
        user = request.user

        # Check if the user has already booked for this bus
        existing_booking = Booking.objects.filter(user=user, bus=bus).first()
        if existing_booking:
            messages.error(request, 'You have already booked for this bus.')
            return redirect('home')  # Redirect to home or wherever you want

        # Generate a random booking ID (you may want a more sophisticated method)
        booking_id = random.randint(1000, 9999)

        # Create a booking for the user and the selected bus
        booking = Booking.objects.create(user=user, bus=bus, booking_id=booking_id, seats=6)  # Assuming 6 seats for now

        # Update the bus to reduce the available seats
        bus.max_capacity -= 6  # Reduce by the number of seats booked
        bus.save()

        # Render the booking page with necessary information
        return render(request, 'booking.html', {'booking': booking, 'total_amount': bus.price * 6})

    # If the request method is not POST, render the book_tickets template
    return render(request, 'book_tickets.html', {'bus': bus})

# ... other views ...

# views.py

from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from .models import Booking

def confirm_booking(request):
    if request.method == 'POST':
        booking_id = request.POST.get('booking_id')
        booking = get_object_or_404(Booking, booking_id=booking_id)

        # Assuming you have a confirm_booking template for displaying success message
        return render(request, 'confirm_booking.html', {'booking': booking})

    messages.error(request, 'Invalid request method.')
    return redirect('home')  # Redirect to home or wherever you want






