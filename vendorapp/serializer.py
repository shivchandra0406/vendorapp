from django.db.models import fields
from rest_framework import serializers
from .models import *
from django.contrib.gis.geos import Point
from geopy.geocoders import Nominatim
from rest_framework_gis.serializers import GeoFeatureModelSerializer
geolocator = Nominatim(user_agent="location")

class VerndorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vendor
        fields='__all__'

class HotelSerializer(GeoFeatureModelSerializer):
    #distance = serializers.CharField()
    class Meta:
        model =Hotel
        fields ='__all__'
        geo_field='location'
        #read_only_fields=['distance']
    
class HotelSerializer1(serializers.ModelSerializer):
    class Meta:
        model=Hotel
        fields=['name','address','location','distance']
        #fields='__all__'
class ModifySerializer(serializers.Serializer):
    lat=serializers.FloatField()
    lag=serializers.FloatField()
    # lat=serializers.CharField()
    # lag=serializers.CharField()
