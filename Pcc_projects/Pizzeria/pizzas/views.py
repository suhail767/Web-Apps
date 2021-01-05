from django.shortcuts import render
from .models import Pizza
from .models import Topping


def index(request):
    """The home page for Pizzeria"""
    return render(request, 'pizzas/index.html')


def pizzas(request):
    """Show all Pizzas"""
    pizza_type = Pizza.objects.order_by('date_added')
    context = {'pizza_type': pizza_type}
    return render(request, 'pizzas/pizza_type.html', context)


def pizza(request, pizza_id):
    """Show a single pizza and all its toppings."""
    toppings = Topping.objects.all()
    context = {'toppings': toppings}
    return render(request, 'pizzas/pizza.html', context)
