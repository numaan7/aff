from django.shortcuts import render
from .models import Product, Blog


def index(request):
    products = Product.objects.all()    
    blogs = Blog.objects.all()[:4]

    return render(request, 'index.html', context={'products': products, 'allblogs':blogs})


def products(request):
    products = Product.objects.all()    
    print(products)
    return render(request, 'products.html', context={'products': products})


def about(request):
    return render(request, 'about.html', context={'products': products})


def services(request):
    return render(request, 'services.html')

def client(request):
    return render(request, 'client.html', context={'products': products})


def contact(request):
    return render(request, 'contact.html')

def blogbytitle(request, posttitle):
    blog = Blog.objects.get(title=posttitle)
    return render(request, 'blog.html', context={'blog':blog})

def blogs(request):
    blog = Blog.objects.all()
    return render(request, 'blogs.html', context={'allblogs':blog})