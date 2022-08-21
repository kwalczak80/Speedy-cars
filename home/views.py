from django.shortcuts import render
from django.http import HttpResponse
from cars.models import Car
from employees.models import Employee
from cars.choices import make_choices, fuel_type_choices, body_type_choices, engine_size_choices, price_choices

def index(request):
    return render(request, 'pages/index.html')

def about(request):
    employees = Employee.objects.all()

    context = {
        'employees': employees
    }
    return render(request, 'pages/about.html', context)

def search(request):
    cars = Car.objects.order_by('-date').filter(is_for_sale=True)[:3]

    context = {
        'cars': cars,
        'make_choices': make_choices,
        'fuel_type_choices': fuel_type_choices,
        'body_type_choices': body_type_choices,
        'engine_size_choices': engine_size_choices,
        'price_choices': price_choices
    }
    return render(request, 'pages/search.html', context)


