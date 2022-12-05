

# Create your views here.
from django.shortcuts import render

from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
 return render(request,'home.html')

def about(request):
 return render(request,'about.html')

def Realstate(request):
  return render(request, 'Realstate.html')

def Yacht(request):
  return render(request, 'Yacht.html')

def Car(request):
  return render(request, 'Car.html')

def Jet(request):
  return render(request, 'Jet.html')





