# """ define url pattern for users"""

from django.urls import path, include

from . import views

app_name = 'users'
urlpatterns = [
    #include deafult auth URLs
    path('', include('django.contrib.auth.urls')),
    #registartion page
    path('register/', views.register, name='register'),
]
