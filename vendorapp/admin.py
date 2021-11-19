#from __future__ import unicode_literals
from django.contrib.gis import admin
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.auth.admin import UserAdmin
from .models import *
# Register your models here.
# @admin.register(Vendor)
# class VendorAdmin(admin.ModelAdmin):
#     list_display=['name','mobilenumber','email','location','service','address','aadharImage','panImage','gstImage','land_line','accountNumber'
#     ,'ifsc_code','accountName','bankName','timing','about','logo']
class HotelAdmin(admin.OSMGeoAdmin):
    model = Hotel
    list_display = ['name','address','location']
    #search_fields = ['first_addr','second_addr','town','state','zip_code']

admin.site.register(Hotel,HotelAdmin)

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display=['city','location']
