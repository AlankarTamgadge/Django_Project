from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.views import View
from .models import Product,Cart, Customer, OrderPlaced
from .forms import CustomerRegistrationForm, CustomerLoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.



class ProductView(View):
    def get(self,request):
        topwears = Product.objects.filter(category="TW")
        bottomwears = Product.objects.filter(category="BW")
        mobiles = Product.objects.filter(category="M")

        
        return render(request,'app/home.html',{'topwears':topwears,'bottomwears':bottomwears, 'mobiles':mobiles})

    


class ProductDetailsView(View):
    def get(self, request,pk):
        product = Product.objects.get(pk=pk)
        return render(request,'app/productdetail.html',{'product':product})


def mobile(request,data=None):
    if data == None:
        mobiles = Product.objects.filter(category="M")
    elif data == 'redmi' or data == 'Samsung':
        mobiles = Product.objects.filter(brand=data)

    return render(request,'app/mobile.html',{'mobiles':mobiles})



class CustomerRegistrationView(View):
    def get(self,request):
        form = CustomerRegistrationForm()
        return render(request,'app/customerregistration.html',{'form':form})


    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request,"Successfully Registered")
            form.save()
        form = CustomerRegistrationForm()
        return render(request,'app/customerregistration.html',{'form':form})

        

 
class CustomerLoginView(View):
    def get(self,request):
        form = CustomerLoginForm()
        return render(request,'app/customerlogin.html',{'form':form})


    def post(self, request):
        form = CustomerLoginForm(request=request,data=request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            upass = form.cleaned_data['password']
            user = authenticate(username=uname,password=upass)

            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/')
        return render(request,'app/customerlogin.html',{'form':form})
    
    
    
    
def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile1(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password1(request):
 return render(request, 'app/changepassword.html')

def mobile1(request):
 return render(request, 'app/mobile.html')

def login1(request):
 return render(request, 'app/login.html')

def customerregistration1(request):
 return render(request, 'app/customerregistration.html')

def checkout1(request):
 return render(request, 'app/checkout.html')
        
