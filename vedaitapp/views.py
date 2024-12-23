from django.shortcuts import render
from  vedaitapp.models import Admission
# Create your views here.
def IndexPage(request):
    return render(request,"app/index.html",{})

def Login(request):
    return render(request,"app/login.html",{})

def Product(request):
    data = Admission.objects.all()
    return render(request,"app/product.html",{'data':data})

def Service(request):
    return render(request,"app/service.html",{})

def Transport(request):
    message= "hey hi"
    return render(request,"app/transport.html",{})