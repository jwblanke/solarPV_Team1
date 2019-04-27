from django.shortcuts import render
from django.http import request, JsonResponse
from rest_framework import generics
from ..models import Product, Certificate, Service
from .serializers import ProductSerializer, CertificateSerializer, ServiceSerializer

# Create your views here.
class ProductListView(generics.ListAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer
	
class CertificateListView(generics.ListAPIView):
	queryset = Certificate.objects.all()
	serializer_class = CertificateSerializer

class CertificateDetailView(generics.RetrieveAPIView):
	queryset = Certificate.objects.all()
	serializer_class = CertificateSerializer
	
class ServiceListView(generics.ListAPIView):
	queryset = Product.objects.all()
	serializer_class = ServiceSerializer

class ServiceDetailView(generics.RetrieveAPIView):
	queryset = Product.objects.all()
	serializer_class = ServiceSerializer

def certificate_search(request):
	search_param = request.GET.get('search_param', '')
	serialized_data =  {'certificate': None}
	if search_param == '':
		return JsonResponse(serialized_data)

	if search_param.isdigit():
		queryset = Certificate.objects.filter(certNumber=int(search_param)).first()
		serializer_class = CertificateSerializer(queryset, many=False)
		serialized_data['certificate'] = serializer_class.data

	if serialized_data['certificate'] != None:
		return JsonResponse(serialized_data)

	product = Product.objects.filter(name=search_param).first()
	if product != None:
		certificate = Certificate.objects.filter(productID=product.id).first()
		serializer_class = CertificateSerializer(certificate, many=False)
		serialized_data['certificate'] = serializer_class.data

	return JsonResponse(serialized_data)