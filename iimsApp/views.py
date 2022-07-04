from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import get_user_model
# from iimsApp.models import Events
from django.db import connection
User = get_user_model()

# Create your views here.

def showDemoPage(request):
    return render(request,"demo.html")

def showLoginPage(request):
    return render(request,"login.html")

    # prn = models.CharField(primary_key=True,max_length=255)
    # student_name = models.CharField(max_length=255)
    # student_email = models.EmailField(max_length=100)
    # password = models.CharField(max_length=100)
    # student_phone = models.CharField(max_length=100)
    # semester = models.CharField(max_length=100)
    # track = models.CharField(max_length=255)
    # year = models.IntegerField()
    # objects = models.Manager()


def register(request): 
    if request.method == "POST":
        prn = request.POST['prn']
        student_name = request.POST['student_name']
        student_email = request.POST['student_email']
        student_phone = request.POST['student_phone']
        semester = request.POST['semester']
        track = request.POST['track']
        year = request.POST['year']
        password = request.POST['password']

        user = User.objects.create_user(prn=prn,student_name=student_name,student_email=student_email,student_phone=student_phone,semester=semester,track=track,year=year,password=password)
        user.save();
        print('User created')
        # return redirect('login')
    else:
        return render(request,"register.html")


def login(request):
    if request.method == "POST":
        prn = request.POST['prn']
        password = request.POST['password']
        user = auth.authenticate(prn=prn,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("dashboard")
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')
    else:
        return render(request,"login.html")



def logoutt(request):
    auth.logout(request)
    return redirect("/")