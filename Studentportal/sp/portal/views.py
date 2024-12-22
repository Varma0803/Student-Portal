from django.shortcuts import render
from django.http import HttpResponse
from portal.models import Table
from portal.models import TableBooking
from .forms import TableBookingForm



# Create your views here.

def index(request):
    return  render(request,'portal/index.html')

def about(request):
    return render(request,'portal/about.html')

def menu(request):
    return render(request,'portal/menu.html')

def booktable(request):
    return render(request,'portal/booktable.html')


def index(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        address=request.POST.get('address')
        index=Table(name=name,email=email,address=address)
        index.save()
    return render(request,'portal/index.html')



def booktable(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        booktable=TableBooking(name=name,email=email,phone=phone)
        booktable.save()
    return render(request, 'portal/booktable.html')





