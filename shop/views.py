from django.shortcuts import render
from shop.models import Product

# Create your views here.
def home(request):
    product = Product.objects.all()
    return render(request,"index.html",{"products": product})

def all_products(request):#this is allproduct view function which is used to show all the products in the database
    product = Product.objects.all()
    return render(request,"all products.html",{"products": product})


def sign_in(request):
    return render(request,"login.html")

def sign_up(request):
    return render(request,"sigup.html")
