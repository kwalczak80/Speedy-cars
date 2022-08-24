from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Booking

def booking(request):
    if request.method == 'POST':
        car = request.POST['car']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        booking_obj = Booking(car=car, name=name, email=email, phone=phone, message=message)

        booking_obj.save()
        messages.add_message(request, messages.INFO, 'Congratulations !! You have booked your test drive succesfuly !!')
        return redirect('/cars')



       
