# models.py

from django.db import models
from django.contrib.auth.models import User
from adminapp.models import Bus

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    # Add other necessary fields for your booking, such as seat numbers, etc.
    # ...

    def __str__(self):
        return f"{self.user.username} - {self.bus.bus_name}"
