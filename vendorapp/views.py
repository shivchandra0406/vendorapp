from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from .serializer import *

from rest_framework.views import APIView
from .models import *

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

def saveVendor(request):
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