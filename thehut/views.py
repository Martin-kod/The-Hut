from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking
from .forms import BookingForm

# Create your views here.


def get_homepage(request):
    bookings = Booking.objects.all()
    context = {
        'bookings': bookings
    }
    return render(request, "thehut/thehut_home.html", context)


def book_table(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = BookingForm()
    context = {
        'form': form
    }
    return render(request, "thehut/thehut_booking.html", context)


def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == "POST":
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = BookingForm(instance=booking)
    context = {
        'form': form
    }
    return render(request, 'thehut/edit_booking.html', context)


def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.delete()
    return redirect('home')
