from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout 
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import auth
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from .models import User

# Create your views here.
def register(request):
    if request.method =='POST':
        FirstName = request.POST['fname']
        LastName = request.POST['lname']
        Email = request.POST['email']
        Password = request.POST['psw']
        
        User.objects.create(first_name=FirstName,last_name=LastName,email=Email,password=make_password(Password))
        messages.success(request , "your account is succesfully created")
        return redirect ('index')
    return render(request,'site/login.html')


def login(request):
    if request.method == 'POST':
        Email = request.POST['email']
        Password = request.POST['psw']
        user = auth.authenticate(email=Email,password=Password)
        if user is not None:
            auth.login(request, user)
            messages.success(request , "succesfully log in ")
            return redirect ('index')
        else:
            messages.error(request , "User is not exist ")
            return redirect ('login')    
    return render(request,'site/login.html')