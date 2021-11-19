from location_field.models.spatial import LocationField


from django.contrib.gis.geos import Point
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="location")

def calculate(list,location):
    
    for x in list:
        print("print",x.location.x)