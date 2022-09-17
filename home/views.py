from django.shortcuts import render
from cars.models import Car
from employees.models import Employee
from cars.choices import make_choices, fuel_type_choices, body_type_choices, \
    engine_size_choices, price_choices


def index(request):
    """
    Display main page
    """
    return render(request, 'pages/index.html')


def about(request):
    """
    Display employees details
    on about.html page
    """
    employees = Employee.objects.all()

    context = {
        'employees': employees
    }
    return render(request, 'pages/about.html', context)


def search(request):
    """
    Display three cars recently added
    in the database on search page
    """
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


def error_404(request, exception):
    """
    Customized 404 error page
    to display relevant message
    to the user
    """
    return render(request, 'pages/404.html', status=404)


def error_500(request):
    """
    Customized 500 error page
    to display relevant message
    to the user
    """
    return render(request, 'pages/500.html', status=500)
