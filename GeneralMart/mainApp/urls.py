
from django.contrib import admin
from django.urls import path
from mainApp import views

urlpatterns = [
    path("logout",views.log_out,name="logout"),
    path("register",views.register,name="register"),
    path("login",views.log_in,name="login"),
    path("",views.home,name="home"),
]