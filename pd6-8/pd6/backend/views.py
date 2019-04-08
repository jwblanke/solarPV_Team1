from django.shortcuts import render
from rest_framework import viewsets
from .models import Product, Certificate, Service
from .serializers import ProductSerializer. CertificateSerializer, ServiceSerializer

# Create your views here.
class ProductView(viewsets.ModelViewSet):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer
	
class CertificateView(viewsets.ModelViewSet):
	queryset = Certificate.objects.all()
	serializer_class = CertificateSerializer
	
class ServiceView(viewsets.ModelViewSet):
	queryset = Product.objects.all()
	serializer_class = ServiceSerializer