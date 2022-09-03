from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('cars/', include('cars.urls')),
    path('accounts/', include('allauth.urls')),
    path('booking/', include('booking.urls')),
]

handler404 = 'home.views.error_404'
handler405 = 'home.views.error_405'
