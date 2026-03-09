from django.shortcuts import render
from shop.models import Product

# Create your views here.
def home(request):
    return render(request,"index.html")

def all_products(request):
    product = Product.objects.all()
    return render(request,"all products.html",{"products": product})

