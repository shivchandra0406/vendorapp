from django.urls import path
from .views import *
urlpatterns = [

    path('register/',saveVendor,name='register'),
    path('savelocation/',ListCreateGeneric.as_view()),
    path('login/',LogiView,name='login'),
    path('logout/',logoutView)
    
]