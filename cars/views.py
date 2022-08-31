from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from cars.choices import make_choices, fuel_type_choices, body_type_choices, engine_size_choices, price_choices

from .models import Car

def index(request):
    cars = Car.objects.order_by('-date').filter(is_for_sale=True)
    paginator = Paginator(cars, 3)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)

    context = {
        'cars': paged_cars
    }
    return render(request, 'cars/cars.html', context)

def car(request, car_id):
    car = get_object_or_404(Car, pk=car_id)

    context = {
        'car': car
    }
    return render(request, 'cars/car.html', context)

def search_results(request):
    queryset_list = Car.objects.order_by('-date')
    
    # Keywords query
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)
    
    # Make query
    if 'make' in request.GET:
        make = request.GET['make']
        if make:
            queryset_list = queryset_list.filter(make__icontains=make)
    
    # Fuel Type query
    if 'fuel_type' in request.GET:
        fuel_type = request.GET['fuel_type']
        if fuel_type:
            queryset_list = queryset_list.filter(fuel_type__icontains=fuel_type)
    
    # Body type query
    if 'body_type' in request.GET:
        body_type = request.GET['body_type']
        if body_type:
            queryset_list = queryset_list.filter(body_type__icontains=body_type)
    
    # Engine size query
    if 'engine_size' in request.GET:
        engine_size = request.GET['engine_size']
        if engine_size:
            queryset_list = queryset_list.filter(engine_size__icontains=engine_size)
    
    # Price query
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        'make_choices': make_choices,
        'fuel_type_choices': fuel_type_choices,
        'body_type_choices': body_type_choices,
        'engine_size_choices': engine_size_choices,
        'price_choices': price_choices,
        'cars': queryset_list,
        'values': request.GET
    }

    return render(request, 'cars/search_results.html', context)
