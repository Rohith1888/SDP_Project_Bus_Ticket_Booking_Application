# views.py
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def AdminLogin(request):
    return render(request, "AdminLogin.html")

def AdminDash(request):
    return render(request, "adminDash.html")

def admin_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the admin
        user = authenticate(request, username=username, password=password)

        if user and (user.is_superuser or user.is_staff):
            # If authentication is successful and the user is a superuser or staff, log in and redirect to the admin panel
            login(request, user)
            return redirect('AdminDash')  # Use the correct URL pattern name

        else:
            messages.error(request, 'Invalid username or password. Please try again.')
            return render(request, 'AdminLogin.html')

    return render(request, 'AdminLogin.html')


# views.py

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Bus, BusRoute
from .forms import BusForm, BusRouteForm

# Existing views...

# views.py

from django.shortcuts import render, redirect
from .models import Bus, BusRoute
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from django.http import JsonResponse

from django.shortcuts import render
from .models import Bus

def add_bus(request):
    message = None  # Initialize message variable

    if request.method == 'POST':
        bus_type = request.POST.get('bus_type')
        bus_name = request.POST.get('bus_name')
        bus_number = request.POST.get('bus_number')
        max_capacity = request.POST.get('max_capacity')

        # Check if a bus with the same bus number already exists
        if Bus.objects.filter(bus_number=bus_number).exists():
            # Bus with the same number already exists, set an error message
            message = 'Bus with the same number already exists.'
        else:
            # Create a new bus with not allocated status
            bus = Bus.objects.create(bus_type=bus_type, bus_name=bus_name, bus_number=bus_number, max_capacity=max_capacity, allocated=False)

            # Bus added successfully, set a success message
            message = 'Bus added successfully.'

    return render(request, 'addbus.html', {'message': message})





# views.py

# views.py

# views.py

from django.shortcuts import render, get_object_or_404
from .models import Bus, BusRoute

def add_route(request, not_allocated_buses=None):
    if request.method == 'POST':
        route_name = request.POST.get('route_name')
        source = request.POST.get('source')
        destination = request.POST.get('destination')
        date = request.POST.get('date')
        timings = request.POST.get('timings')
        price = request.POST.get('price')
        selected_bus_number = request.POST.get('bus')  # Get the selected bus number

        try:
            # Get the selected bus and allocate it to the route
            selected_bus = get_object_or_404(Bus, bus_number=selected_bus_number)
            route = BusRoute.objects.create(
                route_name=route_name,
                source=source,
                destination=destination,
                date=date,
                timings=timings,
                price=price,
            )
            route.buses.add(selected_bus)
            route.allocated_bus_number = selected_bus.bus_number
            route.save()

            # Mark the bus as allocated
            selected_bus.allocated = True
            selected_bus.save()

            # Redirect to a success page or handle as needed

        except Bus.DoesNotExist:
            # Handle the case where the selected bus is not found
            return render(request, 'addroute.html', {'not_allocated_buses': not_allocated_buses, 'error_message': 'Selected bus not found'})

    # Render the form page if not a POST request
    not_allocated_buses = Bus.objects.filter(allocated=False)
    return render(request, 'addroute.html', {'not_allocated_buses': not_allocated_buses})






# views.py

from django.shortcuts import render
from .models import Bus

def list_buses(request):
    buses = Bus.objects.all()
    context = {'buses': buses}
    return render(request, 'listbuses.html', context)

def scheduled_buses(request):
    routes = BusRoute.objects.all()
    return render(request, 'scheduledbuses.html', {'routes': routes})

def manage_users(request):
    users = User.objects.all()
    return render(request, 'manage_users.html', {'users': users})

# views.py

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse

def manage_users(request):
    users = User.objects.all()
    return render(request, 'manageusers.html', {'users': users})


# views.py

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse


def edit_user(request, user_id):
    try:
        user = User.objects.get(id=user_id)

        if request.method == 'POST':
            # Handle form submission for updating user details
            user.username = request.POST.get('username')
            user.email = request.POST.get('email')
            user.save()

            return redirect('manage_users')  # Redirect to manage_users page after editing

        return render(request, 'edituser.html', {'user': user})

    except User.DoesNotExist:
        return HttpResponse("User not found")


from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def delete_user(request, user_id):
    try:
        user = User.objects.get(id=user_id)

        if request.method == 'POST':
            # Delete the user from the database
            user.delete()
            return redirect('manage_users')  # Redirect to the manage users page after deletion

        return render(request, 'deleteuser.html', {'user': user})

    except User.DoesNotExist:
        return HttpResponse("User not found")


# views.py

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import AddUserForm

def add_user(request):
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Create a new user
            user = User.objects.create_user(username=username, email=email, password=password)

            # Redirect to the manage users page or handle as needed
            return redirect('manage_users')
    else:
        form = AddUserForm()

    return render(request, 'adduser.html', {'form': form})

# mainapp/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import BusRoute

def edit_route(request, route_id):
    route = get_object_or_404(BusRoute, id=route_id)

    if request.method == 'POST':
        # Process the form submission for editing the route
        # Update the route fields based on the form data
        # Save the changes to the database
        # Redirect to the scheduledbuses page or another appropriate page
        return redirect('scheduled_buses')  # Change 'scheduled_buses' to the actual URL name

    # Render the edit route form with the current route data
    return render(request, 'edit_route.html', {'route': route})


from django.shortcuts import render, get_object_or_404, redirect
from .models import BusRoute

from django.shortcuts import render, get_object_or_404, redirect
from .models import BusRoute

def delete_route(request, route_id):
    route = get_object_or_404(BusRoute, id=route_id)

    if request.method == 'POST':
        # Deallocate buses associated with the route before deleting
        for bus in route.buses.all():
            bus.allocated = False
            bus.save()

        # Delete the route from the database
        route.delete()

        # Redirect to the scheduledbuses page or another appropriate page
        return redirect('scheduled_buses')  # Change 'scheduled_buses' to the actual URL name

    # Render the delete route confirmation page
    return render(request, 'delete_route.html', {'route': route})
from django.shortcuts import get_object_or_404, redirect
from .models import Bus

# views.py
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from .models import Bus

# views.py
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from .models import Bus

def delete_bus(request, bus_id):
    bus = get_object_or_404(Bus, id=bus_id)

    if request.method == 'POST':
        if bus.allocated:
            messages.error(request, f'Cannot delete the bus {bus.bus_name}. It is allocated for a route.')
        else:
            bus.delete()
            messages.success(request, f'The bus {bus.bus_name} has been successfully deleted.')
            return redirect('list_buses')  # Change 'list_buses' to the actual URL name

    return render(request, 'delete_bus.html', {'bus': bus})














