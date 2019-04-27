from django.contrib import admin
from .models import Product, Certificate, Client, Location, TestStandard
import os
# Register your models here.
admin.site.register(Product)
admin.site.register(Certificate)
admin.site.register(Client)
admin.site.register(Location)
admin.site.register(TestStandard)

dirname = os.path.dirname(__file__)
login_template = os.path.join(dirname, '../solarPV/templates/registration/login.html')
admin.site.login_template = login_template
admin.site.site_header = 'SolarPV Dashboard'
admin.site.site_url = '/solarPV'
