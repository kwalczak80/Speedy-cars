from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Car

def index(request):
    cars = Car.objects.order_by('-date').filter(is_for_sale=True)
    paginator = Paginator(cars, 6)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)

    context = {
        'cars': paged_cars
    }
    return render(request, 'cars/cars.html', context)

def car(request, car_id):
    return render(request, 'cars/car.html')

def search(request):
    return render(request, 'cars/search.html')
