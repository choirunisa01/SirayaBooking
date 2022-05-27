from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_user, name='login'),
    path('home', views.home, name='home'),
    path('book', views.book, name='book'),
    path('yourbook', views.yourbook, name='yourbook'),
    path('register_user', views.register_user, name='register_user'), 
    path('jadwal', views.jadwal, name='jadwal'),
    path('about', views.about, name='about'),
    path('help', views.help, name='help'),
    path('detailjadwal', views.detailjadwal, name='detailjadwal'),
]
