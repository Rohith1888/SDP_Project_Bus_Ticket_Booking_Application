# urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path("AdminLogin/", AdminLogin, name='AdminLogin'),  # Use the correct view name
    path("AdminDash/", AdminDash, name='AdminDash'),
    path("admin_login_view/", admin_login_view, name='admin_login_view'),
    path('addbus/', add_bus, name='add_bus'),
    path('addroute/', add_route, name='add_route'),
    path('listbuses/', list_buses, name='list_buses'),
    path('scheduledbuses/', scheduled_buses, name='scheduled_buses'),
    path('manageusers/', manage_users, name='manage_users'),
    path('edituser/<int:user_id>/', edit_user, name='edit_user'),
    path('deleteuser/<int:user_id>/', delete_user, name='delete_user'),
    path('adduser/', add_user, name='add_user'),
path('edit_route/<int:route_id>/', edit_route, name='edit_route'),
    path('delete_route/<int:route_id>/', delete_route, name='delete_route'),
path('delete_bus/<int:bus_id>/', delete_bus, name='delete_bus'),


]
