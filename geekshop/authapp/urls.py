from django.urls import path

from authapp.views import login, register, logout

app_name = 'authapp'
urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('login/', logout, name='logout'),
]
