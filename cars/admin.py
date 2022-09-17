from django.contrib import admin
from .models import Car


class CarAdmin(admin.ModelAdmin):
    """
    Admin class for Cars to display
    specific fields in the admin panel
    """
    list_display = ('id', 'title', 'is_for_sale', 'price', 'date')
    list_display_links = ('id', 'title')
    list_editable = ('is_for_sale',)
    search_fields = ('title', 'make', 'description', 'price', 'year')
    list_per_page = 20


admin.site.register(Car, CarAdmin)
