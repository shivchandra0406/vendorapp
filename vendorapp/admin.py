from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display=['name','mobilenumber','email','location','service','address','aadharImage','panImage','gstImage','land_line','accountNumber'
    ,'ifsc_code','accountName','bankName','timing','about','logo']