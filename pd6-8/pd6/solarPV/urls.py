from django.urls import path

from. import views

urlpatterns = [
    path('solarPV/', views.solarPV, name='solarPV'),
    path('registrationForm/', views.registrationForm, name='registrationForm')
]
