from django.conf.urls import url
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.urls.conf import path
from django.views.generic.base import RedirectView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

from .serializer import *
from rest_framework import generics
from rest_framework.views import APIView
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D,Distance
from geopy.geocoders import Nominatim
from .tester import *
class VendorView(APIView):
    def post(self,request):
        try:
            data=request.data
            serializer=VerndorSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':serializer.data})
            else:
                return Response({'message':serializer.errors},status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({
                'message':'somthing went wrong'
            },status=status.HTTP_400_BAD_REQUEST)
@login_required(login_url='login')
def saveVendor(request):
    # if not request.user.is_authenticated:
    #     return HttpResponse("<h2>First you have Login after move on</h2>")
    #     return render(request,'vendorapp/login.html')
    # else:
    #     print(request.user)
        if request.method=='GET':
            return render(request,'vendorapp/index.html')
        else:
            v=Vendor()
            
            v.name=request.POST.get('name')
            v.mobilenumber=request.POST.get('mobilenumber')
            v.email=request.POST.get('email')
            v.location=request.POST.get('location')
            v.service=request.POST.get('service')
            v.address=request.POST.get('address')
            v.land_line=request.POST.get('land_line')
            v.aadharImage=request.POST.get('aadhar')
            v.panImage=request.POST.get('pan')
            v.gstImage=request.POST.get('gst')
            v.accountNumber=request.POST.get('accountNumber')
            v.bankName=request.POST.get('bankName')
            v.ifsc_code=request.POST.get('ifsc_code')
            v.accountName=request.POST.get('accountName')
            v.otherservice=request.POST.get('otherservice')
            v.about=request.POST.get('about')
            v.logo=request.POST.get('logo')
            v.save()
            return HttpResponse("Registration successfully")

def LogiView(request):
    try:
        if request.method=='GET':
            return render(request,'vendorapp/login.html')
        else:
            username=request.POST.get('username')
            print(username)
            obj=User.objects.filter(username=username).first()
            if obj is None:
                return HttpResponse("Your email is not valid")
            else:
                password=request.POST.get('password')
                user=authenticate(request,username=username,password=password)
                if user is not None:
                    login(request,user)
                    #return render(request,'vendorapp/index.html')
                    return redirect('register')
                else:
                   return HttpResponse("your email and password are wrong")
                    
    except Exception as e:
        print(e)
        return HttpResponse("somthing went wrong")

def logoutView(request):
    if request.method=='POST':
        logout(request)
        return redirect('login')


geolocator = Nominatim(user_agent="location")


class ListCreateGeneric(APIView):
    def post(self,request):
        try:
            data=request.data
            #print(data)
            serilalizer=HotelSerializer1(data=data)
            if serilalizer.is_valid():
                
                serilalizer.save()
                print(serilalizer.data['location'])
                return Response({'message':serilalizer.data})
            return Response({'message':serilalizer.errors})
        except Exception as e:
            print(e)
            return Response({'message':"somthing went wrong"})
    # def printData(result):
    #     for x in result:
    #         print(x)
    def get(self,request):
        try:
            distance = 100
            data=request.data
            #print(data)
            s=ModifySerializer(data=data)
            #print(s)
            ref_location=0
            if s.is_valid():
                p1=s.data['lat']
                p2=s.data['lag']
                print(s.data['lat'],s.data['lag'])
                print(type(p1))
                ref_location=Point(p2,p1)
                
            else:
                return Response({"message":s.errors})
            #ref_location = Point(12.873291,77.651255)
            print(ref_location)   
            res = Hotel.objects.filter(
            location__distance_lt =(
            ref_location,
            D(m=distance)
            )
            )
            #calculate(res,data['location'])
            serializer=HotelSerializer1(res,many=True)
            return Response({'message':serializer.data})
            #return Response({'message':serializer.errors})
        except Exception as e:
            print(e)
            return Response({'message':"somthing went wrong"})
    

    # def perform_create(self, serializer):
    #     address = serializer.initial_data["address"]
    #     g = geolocator.geocode(address)
    #     lat = g.latitude
    #     lng = g.longitude
    #     pnt = Point(lng, lat)
    #     print(pnt)
    #     serializer.save(location=pnt)
