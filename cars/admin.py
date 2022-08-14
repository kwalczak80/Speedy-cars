from django.contrib import admin
from .models import Car

class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_for_sale', 'price', 'date')


admin.site.register(Car, CarAdmin)

