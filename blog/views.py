from django.shortcuts import render,redirect
from .models import *
from blog.forms import *
# Create your views here.

def home(request):
    return render(request, 'index.html')

def cars(request):
    cars = Cars.objects.all()
    context = {
        'cars': cars
    }
    return render(request, 'smallCars.html', context)

def corporativClient(request):
    return render(request, 'corporativClient.html')

def special(request):
    return render(request, 'special.html')

def public(request):
    return render(request, 'public.html')

def about(request):
    return render(request, 'about-company.html')

def service(request):
    return render(request, 'service.html')

def repair(request):
    return render(request, 'repair.html')

def spareparts(request):
    return render(request, 'spareparts.html')

def orderparts(request):
    return render(request, 'orderparts.html')

def garant(request):
    return render(request, 'garant.html')

def contact(request):
    return render(request, 'contact.html')

def carDetail(request, pk):
    car = Cars.objects.get(id=pk)
    context = {
        'car': car
    }
    return render(request, 'carDetail.html', context)

def zakaz(request):
    if request.method == "POST":
        error = ''
        form = DetailForm(request.POST)
        if form.is_valid():
          form.save()
          return redirect('home')
        else:
           error = "Page not found"
    form = DetailForm()
    context = {
        'form':form
    }
    return render(request, 'zakaz.html',context)


def signIn(request):
    return render(request, 'signin.html')



def signUp(request):
    return render(request, 'signup.html')




