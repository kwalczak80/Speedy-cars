from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Booking
from .forms import BookingForm


def booking(request):
    """
    The booking function evaluates the user entries.
    If all user entries are valid the test drive is
    saved in the database otherwise, it is canceled.
    """
    if request.method == 'POST':
        car = request.POST['car']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        test_drive_date = request.POST['date']
        date = datetime.strptime(test_drive_date,
                                 "%d/%m/%Y").strftime('%Y-%m-%d')
        message = request.POST['message']
        user_id = request.POST['user_id']
        car_id = request.POST['car_id']
        test_drive_booked = Booking.objects.all().filter(car_id=car_id,
                                                         user_id=user_id)
        if test_drive_booked:
            messages.add_message(request, messages.ERROR,
                                 "You have booked a test drive "
                                 "with this car already !!")
            return redirect('/cars/'+car_id)
        if date >= datetime.today().strftime('%Y-%m-%d'):
            booking_obj = Booking(car=car, name=name, email=email, phone=phone,
                                  date=date, message=message, user_id=user_id,
                                  car_id=car_id)
            booking_obj.save()
            messages.add_message(request, messages.SUCCESS,
                                 "Congratulations !! You have booked your "
                                 "test drive successfully.")
            return redirect('/cars/'+car_id)
        else:
            messages.add_message(request, messages.ERROR, "Selected date is "
                                                          "in the past, please"
                                                          " choose a date in"
                                                          " the future.")
            return redirect('/cars/'+car_id)


def dashboard(request):
    """ Display all booked test drives in the dashboard """
    user_booking = Booking.objects.all().filter(user_id=request.user.id)

    context = {
        'booking': user_booking
    }
    return render(request, 'booking/dashboard.html', context)


def cancellation(request, booking_id):
    """ Deletes the booking from the database using it's primary key """
    booking_cancellation = get_object_or_404(Booking, pk=booking_id)
    if request.method == 'POST':
        booking_cancellation.delete()
        messages.add_message(request, messages.INFO, "Your test drive "
                                                     "has been cancelled.")
        return redirect('dashboard')
    return render(request, 'booking/booking_cancellation.html')


def edit(request, booking_id):
    """ The view for user to be able to edit their existing bookings """
    booking_id = get_object_or_404(Booking, pk=booking_id)
    if request.method == "POST":
        form = BookingForm(request.POST, instance=booking_id)
        if form['date'].value() >= datetime.today().strftime('%Y-%m-%d'):
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.INFO,
                                     "You have edited your test drive "
                                     "details succesfully.")
                return redirect('dashboard')
        else:
            messages.add_message(request, messages.ERROR,
                                 "Selected date is "
                                 "in the past, please"
                                 " choose a date in"
                                 " the future.")
            return redirect('dashboard')
    form = BookingForm(instance=booking_id)
    context = {
        'form': form
    }
    return render(request, 'booking/edit.html', context)
