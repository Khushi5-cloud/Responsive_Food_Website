from django.shortcuts import render
from foodie_app.models import ContactUs,CustomerDetail_Order
from django.contrib import messages



# Create your views here.
def home(request):
    if request.method == "POST":
        name=request.POST.get("name")
        phone=request.POST.get('phone')
        email=request.POST.get("email")
        message=request.POST.get("message")
        con=ContactUs(name=name,phone=phone,email=email,message=message)
        con.save()
        
    return render(request,'index.html')

def order(request):
    if request.method == "POST":
        name=request.POST.get("name")
        phone=request.POST.get('phone')
        email=request.POST.get("email")
        address=request.POST.get("address")
        city=request.POST.get("city")
        state=request.POST.get('state')
        food=request.POST.get("food")
        num=request.POST.get("num")
        con=CustomerDetail_Order(name=name,phone=phone,email=email,address=address,city=city,state=state,food=food,num=num)
        messages.success(request,'Your order has been taken successfully!!')
        con.save()
      
    
    return render(request,'order.html')



def recipe(request):
    return render(request,'Recipe.html')
    
