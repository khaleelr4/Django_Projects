from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('' , views.index , name='home'),
    path('contact' , views.contact , name='contact'),
    path('signup' , views.handlesignup , name='handlesignup'),
    path('signin' , views.handlesignin , name='handlesignin'),
    path('signout' , views.handlesignout , name='handlesignout')
]