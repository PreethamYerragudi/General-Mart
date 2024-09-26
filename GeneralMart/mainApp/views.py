from django.shortcuts import render
from django.http import HttpResponse
from mainApp.forms import RegisterForm, Login
from .models import User
# Create your views here.

def register(request):
    form = RegisterForm
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
    content = {"form":form, "type":"Register"}
    return render(request,"userForm.html",content)

def login(request):
    form = Login
    if request.method == 'POST':
        form = Login(request.POST)
        if form.is_valid():
            if User.objects.filter(email=request.POST.get('username')).exists():
                if User.objects.filter(email=request.POST.get('username')).values("password").get()['password'] == request.POST.get('password'):
                    print("User Logged In")
                else:
                    print("Incorrect password")
            else:
                print("No such user")
    content = {"form":form, "type":"Login"}
    return render(request, "userForm.html", content)
