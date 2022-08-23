from django.shortcuts import render, redirect
from .models import Booking

def booking(request):
    if request.method == 'POST':
        car = request.POST['car']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        booking = Booking(car=car, name=name, email=email, phone=phone, message=message)

        booking.save()
        return redirect('/cars')



       
