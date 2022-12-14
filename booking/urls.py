from django.urls import path
from . import views

urlpatterns = [
    path('booking', views.booking, name='booking'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('cancellation/<booking_id>/', views.cancellation,
         name='cancellation'),
    path('edit/<int:booking_id>/', views.edit, name='edit'),
]
