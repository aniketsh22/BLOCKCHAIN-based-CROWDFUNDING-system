from django.shortcuts import redirect, render
from unicodedata import name
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import PasswordChangeForm
import csv

def index(request):
    return render(request,"index.html")

def connect(request):
    return render(request,"connect.html")

def my_redirect(request):
    return redirect("https://forms.gle/yZigZieRMuphmtuc6")

def signin(request):
    return render(request,"signin.html")

def aboutus(request):
    return render(request,"aboutus.html")

def contact(request):
    return render(request,"contact.html")

def project(request):
    return render(request,"project.html")

def register(request):

    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1==pass2:
            if User.objects.filter(username=username).exists():
                messages.success(request,'username already exists! Try with another username')
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.success(request,'Email already exists! Try with another email')
                return redirect('register')
            else:
                myuser = User.objects.create_user(username=username, password=pass1, email=email)
                myuser.first_name = fname
                myuser.last_name = lname
                myuser.save()
                messages.success(request, "Your account has been registered successfully! Please login to continue.")
                return redirect('login')

        else:
             messages.success(request,'Password not matching :(')
        return redirect('register')
    else:
        return render(request,"register.html")


def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password = request.POST['pass1']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.success(request,'Invalid Credentials')
            return redirect('login')
    else:
        return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


#Donate pages
def donate1(request):
    return render(request,"donate1.html")

def donate2(request):
    return render(request,"donate2.html")

def donate3(request):
    return render(request,"donate3.html")


