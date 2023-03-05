from django.shortcuts import render
from .models import Product


def index(request):
    products = Product.objects.all()    

    return render(request, 'index.html', context={'products': products})


def products(request):
    products = Product.objects.all()    
    print(products)
    return render(request, 'products.html', context={'products': products})


def about(request):
    return render(request, 'about.html', context={'products': products})


def client(request):
    return render(request, 'client.html', context={'products': products})


def contact(request):
    return render(request, 'contact.html')