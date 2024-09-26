from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request, product_id):
    products = [
        "Air Bag",
        "Dirt Bike",
        "Wizard Wand"
    ]

    response = HttpResponse(f"{products[product_id]}")
    return HttpResponse(response)
