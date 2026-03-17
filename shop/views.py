from django.shortcuts import render,redirect
from shop.models import Product

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout

# Create your views here.
def home(request):
    product = Product.objects.all()
    return render(request,"index.html",{"products": product})

def all_products(request):#this is allproduct view function which is used to show all the products in the database
    product = Product.objects.all()
    return render(request,"all products.html",{"products": product})


def sign_in(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request,user)
            return redirect("home")
        else:
            return render(request,"login.html",{"error": "Invalid username or password"})

    return render(request,"login.html")

def sign_up(request):
    if request.method == "POST":
        fname = request.POST.get("Firstname")
        lname = request.POST.get("Lastname")
        uname = request.POST.get("Username")
        email = request.POST.get("Email")
        password = request.POST.get("Password")
        cpassword = request.POST.get("ConfirmPassword")
        if password != cpassword:
            return render(request,"sigup.html",{"error":"Password and Confirm Password do not match"})
        
        if User.objects.filter(username=uname).exists():
            return render(request,"sigup.html",{"error":"Username already exists"})
        if User.objects.filter(email=email).exists():
            return render(request,"sigup.html",{"error":"Email already exists"})
        
        user = User.objects.create_user(username=uname, email=email, password=password, first_name=fname, last_name=lname)
        user.save()
        return redirect("login")
    
    return render(request,"sigup.html")
    

def sign_out(request):
    logout(request)
    return redirect("home")
        

def product_details(request,p_id):
    data = Product.objects.get(id=p_id)
    return render(request,"productdeatails.html",{"data": data})    




    
