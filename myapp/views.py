from django.shortcuts import render
from .models import Product

def index(request):
    products = Product.objects.all()  # Get all products from the database
    context = {'products': products} 
    return render(request, 'myapp/index.html', context)

def about(request):
    context = {'message': 'About page'}  # Context is created HERE
    return render(request, 'myapp/about.html', context)

def contact(request):
    context = {'message': 'Contact page'}  # Context is created HERE
    return render(request, 'myapp/contact.html', context)

