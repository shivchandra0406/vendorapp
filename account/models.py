from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import *
# Create your models here.
"""We define Abstract model"""

class BaseModel(models.Model):
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)
    class Meta:
        abstract:True
"""End Defineing Abstract model"""

"""We have define Customer Registration"""
def generateRegistrationId():
    try:
        obj=CustomerRegistration.objects.all().last()
        if obj is None:
            return obj.customer_id+1
        else:
            return 1000
    except Exception as e:
        print(e)
class CustomerRegistration(AbstractUser):
    username=None
    password=None
    customer_id=models.IntegerField(default=generateRegistrationId,primary_key=True,editable=False)
    mobileNumber=models.CharField(max_length=13,unique=True)
    email=models.EmailField(null=True,blank=True)
    dob=models.DateField(null=True,blank=True)
    gender=models.CharField(max_length=30,null=True,blank=True,choices=(('Male','Male'),('Female','Female')))
    otp=models.IntegerField(default=0)

    USERNAME_FIELD='mobileNumber'
    REQUIRED_FIELDS=[]
    objects=UserManager()


class CustomerAddress(BaseModel):
    customers=models.ForeignKey(CustomerRegistration,related_name='customer_address',on_delete=models.CASCADE)
    fullName=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    address=models.CharField(max_length=100)
    pincode=models.CharField(max_length=20)
    city=models.CharField(max_length=50)
    servicelocation=models.CharField(max_length=100)
    select_service_location=models.CharField(max_length=50,choices=(('Add as Home','Add as Home'),('Add as Office','Add as Office')))
