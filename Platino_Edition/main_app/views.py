

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

def realstates(request):
  return render(request, 'realstates.html')

def yachts(request):
  return render(request, 'yachts.html')

def car(request):
  return render(request, 'car.html')

def jets(request):
  return render(request, 'jets.html')





