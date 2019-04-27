from django.shortcuts import render
from django.http import request, JsonResponse
import urllib.request
from django.http import HttpResponse
import json

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

def TestingCertification(request):
	return render(request, 'solarPV/TestingCertification.html')

def certificate_search(request):
	search_param = request.GET.get('certificate_search_input', '')
	#todo: hit endpoint, display info
	url =  'https://' if request.is_secure() else 'http://'
	url += request.get_host()
	url += f'/api/search/certificates?search_param={search_param}'

	contents = urllib.request.urlopen(url).read()
	dic = json.loads(contents)
	certificate = dic['certificate']

	return render(request, 'solarPV/TestingCertification.html', {'certificate': certificate})

	
