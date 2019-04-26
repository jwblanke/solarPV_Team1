from django.urls import path, re_path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from. import views

urlpatterns = [
    path('solarPV/', views.solarPV, name='solarPV'),
    path('RegistrationForm/', views.RegistrationForm, name='RegistrationForm'),
    path('Certificate/', views.Certificate, name='Certificate'),
    path('Client/', views.Client, name='Client'),
    path('Location/', views.Location, name='Location'),
    path('Map/', views.Map, name='Map'),
    path('Product/', views.Product, name='Product'),
    path('TestStandard/', views.TestStandard, name='TestStandard'),
    re_path('Login/', auth_views.LoginView.as_view(), name='Login')

]
