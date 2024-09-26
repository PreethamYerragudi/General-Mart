
from django.contrib import admin
from django.urls import path
from mainApp import views

urlpatterns = [
    path("<int:product_id>",views.home,name="home"),
]