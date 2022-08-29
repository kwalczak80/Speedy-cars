from django.urls import path

from . import views

urlpatterns = [
    path('booking', views.booking, name='booking'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('<booking_id>', views.cancellation, name='cancellation'),
]