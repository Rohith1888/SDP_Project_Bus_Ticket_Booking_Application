# forms.py

from django import forms
from .models import Bus, BusRoute

class BusForm(forms.ModelForm):
    class Meta:
        model = Bus
        fields = ['bus_type', 'bus_name', 'bus_number', 'max_capacity']

class BusRouteForm(forms.ModelForm):
    class Meta:
        model = BusRoute
        fields = ['route_name', 'source', 'destination', 'date', 'timings', 'price']


# forms.py

from django import forms

class AddUserForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

# forms.py
from django import forms
from .models import BusRoute

class EditBusRouteForm(forms.ModelForm):
    class Meta:
        model = BusRoute
        fields = '__all__'

