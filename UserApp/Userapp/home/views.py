from django.shortcuts import render , HttpResponse , redirect
from django.contrib import messages 
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import User


# Create your views here.

def index(request):
    return render(request , 'index.html')

def contact(request):
    return render(request , 'contact.html')

def handlesignup(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        username = request.POST['username']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # checking of the error logics
        if len(fname)<5:
            messages.error(request , 'Enter Your Correct First Name')
            return redirect ("home")
        
        if len(lname)<5:
            messages.error(request , 'Enter Your Correct Last Name')
            return redirect ("home")

        # if email==email:
        #     messages.error(request , 'Email Already Exists')
        #     return redirect ("home")

        if len(email)<5:
            messages.error(request , 'Enter your Correct Email')
            return redirect ("home")

        if not username.isalnum():
            messages.error(request , 'Your Username Does Not Contain Alpha Numeric Characters')
            return redirect ("home")

        if pass1 != pass2:
            messages.error(request , 'Enter your correct password')
            return redirect ("home")

        myuser = User.objects.create_user(email , username , pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, 'Your account has been created')
        return redirect("home")

    return HttpResponse("This is Home page")

def handlesignin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate (username=loginusername , password=loginpassword)

        if user is not None:
             login(request , user)
             messages.success(request , "You are logged in into KBlogs")
             return redirect("home")
        else:
            messages.error(request , "Your credientials are invalid")
            return redirect("home")
        
    return HttpResponse("signin")

def handlesignout(request):
    logout(request)
    messages.success(request , "you are logged out")
    return redirect("home")

    return HttpResponse("signout")