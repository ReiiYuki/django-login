from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User
import django.contrib.auth  as auth

# Create your views here.

def index(request) :
    return render(request,'login/index.html')

def register_view(request) :
    return render(request,'login/register.html')

def success(request) :
    user = request.user
    return render(request,'login/user.html',{'user':user})

def register(request) :
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']
    user = User.objects.create_user(username,email,password)
    user.save()
    return HttpResponseRedirect(reverse('login:index'))

def login(request) :
    if request.POST['action'] == 'Register' :
        return HttpResponseRedirect(reverse('login:register_view'))
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None :
        auth.login(request,user)
        return HttpResponseRedirect(reverse('login:success'))
    else :
        return HttpResponseRedirect(reverse('login:index'))

def logout(request) :
    auth.logout(request)
    return HttpResponseRedirect(reverse('login:index'))
