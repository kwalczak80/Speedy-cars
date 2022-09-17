from django.contrib import admin
from .models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    """
    Admin class for Employee to display
    specific fields in the admin panel
    """
    list_display = ('id', 'name', 'email', 'hire_date')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Employee, EmployeeAdmin)
