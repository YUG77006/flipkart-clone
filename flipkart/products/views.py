from django.shortcuts import render
from .models import Product

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def mobiles(request):
    products = Product.objects.filter(category='mobile')
    return render(request, 'mobile.html', {'products': products})

def fashion(request):
    products = Product.objects.filter(category='fashion')
    return render(request, 'fashion.html', {'products': products})