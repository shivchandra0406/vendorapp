#from django.db import models
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from location_field.models.spatial import LocationField
from location_field.models.plain import PlainLocationField
from django.contrib.gis.db import models
import haversine as hs
from haversine import Unit
from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
from geopy.distance import distance
#from geoposition.fields import GeopositionField
# Create your models here.
class Vendor(models.Model):
    name=models.CharField(max_length=100)
    mobilenumber=models.CharField(max_length=12)
    email=models.EmailField()
    #location=models.CharField(max_length=100)
    service=models.CharField(max_length=100)
    address=models.TextField()
    land_line=models.CharField(max_length=100)
    #kyc=models.CharField(max_length=50,choices=(('Pan','Pan'),('Aadhar','Aadhar'),('Gst','Gst')))
    aadharImage=models.ImageField(upload_to='Aadhar/')
    panImage=models.ImageField(upload_to='Pan/')
    gstImage=models.ImageField(upload_to='gst/')
    accountNumber=models.CharField(max_length=100)
    bankName=models.CharField(max_length=100)
    ifsc_code=models.CharField(max_length=50)
    accountName=models.CharField(max_length=50)
    otherservice=models.CharField(max_length=50)
    timing=models.DateTimeField(auto_now_add=True)
    about=models.CharField(max_length=100)
    location =models.CharField(max_length=50)
    logo=models.ImageField(upload_to='Logo/')

class Hotel(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    location = LocationField(based_fields=['address'], zoom=7) # Spatial Field Types

    def __str__(self) -> str:
        return self.name
    def distance(self):
        
        #print(self.location)
        pnt=Point(77.651255,12.873291)
        #pnt=Point(12.873291,77.651255)
        pnt1=Point(self.location.y,self.location.x)
        
        #return hs.haversine(self.location,pnt,unit=Unit.METERS)
        return distance(pnt,pnt1).m
        # # print(city, d)
class Place(models.Model):
    city = models.CharField(max_length=255)
    location = PlainLocationField(based_fields=['city'], zoom=7)



# @receiver(Get_save, sender=Hotel)
# def my_handler(sender,instance, **kwargs):
#     print("shiv",instance.location)