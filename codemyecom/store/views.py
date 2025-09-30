from django.shortcuts import render, HttpResponse, redirect
from .models import Product, Catagory
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms

# Create your views here.

def catagory(request, foo):
    foo = foo.replace('-' , ' ')
    # grab the catagory form url
    try:
        catagory = Catagory.objects.get(name=foo)
        products = Product.objects.filter(catagory=catagory)
        return render (request, "catagory.html" , {"products":products, "catagory":catagory})
    except:
        messages.success(request, ("Catagory Does Not Exists........."))
        return redirect('home')

def product(request,pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product.html',{'product':product})

def index(request):
    # return  HttpResponse("<h1>this ia a home page httpsresponse homepage</h1>")
    products = Product.objects.all()
    return render(request, "index.html", {"products":products})

def about(request):
    return render(request, "about.html", {})

def login_user(request):
    if request.method == "POST":
        username = request.POST ['username']
        password = request.POST ['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You Have Been Logged In........."))
            return redirect('home')
        else:
            messages.success(request, ("There Was An Error, Please Try Again........."))
            return redirect('login')
    else:
        return render(request, "login.html", {})

def logout_user(request):
    logout(request)
    messages.success(request, ("You Have Been Logged Out...... Thanks"))
    return redirect('home')

def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # login user
            user = authenticate (username=username, password=password)
            login(request, user)
            messages.success(request, ("You Have Resister User Successfully...... Welcome!"))
            return redirect('home')
        else:
            messages.success(request, ("There was an problem...... Register Properly!"))
            return redirect('register')
    else:
        return render(request, "register.html", {'form':form})