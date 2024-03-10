# models.py

# models.py

# models.py

from django.db import models

class Bus(models.Model):
    BUS_TYPE_CHOICES = [
        ('AC', 'AC'),
        ('NON-AC', 'Non-AC'),
    ]

    bus_type = models.CharField(max_length=10, choices=BUS_TYPE_CHOICES)
    bus_name = models.CharField(max_length=100)
    bus_number = models.IntegerField(unique=True)
    max_capacity = models.PositiveIntegerField()
    allocated = models.BooleanField(default=False)  # New field

    def __str__(self):
        return self.bus_name



class BusRoute(models.Model):
    route_name = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    date = models.DateField()
    timings = models.TimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    buses = models.ManyToManyField(Bus)  # Many-to-many relationship

    def __str__(self):
        return self.route_name


