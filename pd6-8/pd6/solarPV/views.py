from django.shortcuts import render

from django.http import HttpResponse

def solarPV(request):
    return render(request, 'solarPV/solarPV.html')

def RegistrationForm(request):
    return render(request, 'solarPV/RegistrationForm.html')

def Certificate(request):
    return render(request, 'solarPV/Certificate.html')

def Client(request):
    return render(request, 'solarPV/Client.html')

def Location(request):
    return render(request, 'solarPV/Location.html')

def Map(request):
    return render(request, 'solarPV/Map.html')

def Product(request):
    return render(request, 'solarPV/Product.html')

def TestStandard(request):
    return render(request, 'solarPV/TestStandard.html')

def Login(request):
    return render(request, 'solarPV/Login.html')
