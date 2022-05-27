from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('booking.urls')),
    # path('', include('django.contrib.auth.urls')),
    path('booking/', include('django.contrib.auth.urls')),
    path('booking/', include('booking.urls')),
]
