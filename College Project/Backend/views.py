from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def AboutPage(request):
    return render (request,'about.html')

def ContactPage(request):
    return render (request,'contact.html')

def SinglePage(request):
    return render (request,'single.html')

def TeacherPage(request):
    return render (request,'teacher.html')

def JoinnowPage(request):
    return render (request,'joinnow.html')

def CoursePage(request):
    return render (request,'course.html')

@login_required(login_url='login')
     
def HomePage(request):
    return render (request,'home.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("your pass and confrom pass are success")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
    

    return render (request,'signup.html')

def LoginPage(request):

    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("username or pass is incorrect!!")
    return render (request,'login.html')

