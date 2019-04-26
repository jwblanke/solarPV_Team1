from django.contrib import admin
from .models import Product, Certificate, Client, Location, TestStandard

# Register your models here.
admin.site.register(Product)
admin.site.register(Certificate)
admin.site.register(Client)
admin.site.register(Location)
admin.site.register(TestStandard)

admin.site.site_header = 'SolarPV Dashboard'
admin.site.site_url = '/solarPV'