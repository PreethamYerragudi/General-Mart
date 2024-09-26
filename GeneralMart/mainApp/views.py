from django.shortcuts import render
from django.http import HttpResponse
from mainApp.forms import RegisterForm
# Create your views here.

def register(request):
    form = RegisterForm
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
    content = {"form":form}
    return render(request,"registration.html",content)
