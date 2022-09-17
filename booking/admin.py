from django.contrib import admin
from .models import Booking


class BookingAdmin(admin.ModelAdmin):
    """
    Admin class for Booking to display
    specific fields in the admin panel
    """
    list_display = ('id', 'user_id', 'name', 'car', 'car_id', 'email', 'phone')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'car')
    list_per_page = 15


admin.site.register(Booking, BookingAdmin)

