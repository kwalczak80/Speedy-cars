from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Booking

def booking(request):
    if request.method == 'POST':
        car = request.POST['car']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        date = request.POST['date']
        message = request.POST['message']
        user_id = request.POST['user_id']

        booking_obj = Booking(car=car, name=name, email=email, phone=phone, date=date, message=message, user_id=user_id)

        booking_obj.save()
        messages.add_message(request, messages.INFO, 'Congratulations !! You have booked your test drive succesfuly !!')
        return redirect('/cars')

def dashboard(request):
    user_booking = Booking.objects.all().filter(user_id=request.user.id)

    context = {
        'booking': user_booking
    }
    return render(request, 'booking/dashboard.html', context)


       
