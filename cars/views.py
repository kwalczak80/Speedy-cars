from django.shortcuts import render

from .models import Car

def index(request):
    cars = Car.objects.all()

    context = {
        'cars': cars
    }
    return render(request, 'cars/cars.html', context)

def listing(request):
    return render(request, 'cars/car.html')

def search(request):
    return render(request, 'cars/search.html')
