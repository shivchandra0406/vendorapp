from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display=['name','mobilenumber','email','location','service','address','land_link','kyc','accountNumber'
    ,'ifsc_code','accountName','bankName','timing','about','logo']