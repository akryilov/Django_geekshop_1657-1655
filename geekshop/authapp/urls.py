from django.urls import path

from authapp.views import login, register, logout, profile
from mainapp.views import products

app_name = 'authapp'
urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('login/', logout, name='logout'),


]
