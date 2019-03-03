from django.shortcuts import render

from django.http import HttpResponse

def solarPV(request):
    return render(request, 'solarPV/solarPV.html')

def registrationForm(request):
    return render(request, 'solarPV/registrationForm.html')
