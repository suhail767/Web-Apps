"""Defines URL patterns for Pizzas"""

from django.urls import path
from . import views

app_name = 'pizzas'

urlpatterns = [
    # Homepage
    path('', views.index, name='index'),
    # Show all Pizzas
    path('pizza_type/', views.pizzas, name='pizza_type'),
    # All types of Toppings for a single pizzas
    path('pizza_type/<int:pizza_id>/', views.pizza, name='pizza'),
]
