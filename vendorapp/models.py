from django.db import models

# Create your models here.
class Vendor(models.Model):
    name=models.CharField(max_length=100)
    mobilenumber=models.CharField(max_length=12)
    email=models.EmailField()
    location=models.CharField(max_length=100)
    service=models.CharField(max_length=100)
    address=models.TextField()
    land_link=models.CharField(max_length=100)
    kyc=models.CharField(max_length=50,choices=(('Pan','Pan'),('Aadhar','Aadhar'),('Gst','Gst')))
    accountNumber=models.CharField(max_length=100)
    bankName=models.CharField(max_length=100)
    ifsc_code=models.CharField(max_length=50)
    accountName=models.CharField(max_length=50)
    timing=models.DateTimeField(auto_now_add=True)
    about=models.CharField(max_length=100)
    logo=models.ImageField(upload_to='Logo/')