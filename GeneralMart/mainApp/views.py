from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from mainApp.forms import RegisterForm, Login
from django.contrib.auth.models import User
# Create your views here.
user = None
loggedIn = False

def register(request):
    form = RegisterForm
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(request.POST.get('first_name')+request.POST.get('last_name'),request.POST.get('email'),request.POST.get('password'))
            return redirect('login')
    content = {"form":form, "type":"Register"}
    return render(request,"userForm.html",content)

def log_in(request):
    form = Login
    if request.method == 'POST':
        form = Login(request.POST)
        if form.is_valid():
            user = authenticate(username=request.POST.get('username'),password=request.POST.get('password'))
            if user is not None:
                login(request,user)
                return redirect('home')
    content = {"form":form, "type":"Login"}
    return render(request, "userForm.html", content)

def home(request):
    if request.user.is_authenticated:
        name = request.user.username
    else:
        name = "Unkown - Please Log In"
    content = {'name':name}
    return render(request, "home.html",content)

def log_out(request):
    logout(request)
    return redirect('home')
        