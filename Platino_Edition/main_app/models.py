from django.db import models
from django.urls import reverse
from datetime import date
# Import the User
from django.contrib.auth.models import User

class Car(models.Model):
    brand = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    year = models.IntegerField(max_length=4)
    description = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=8, decimal_places=3)
    Images = models.ImageField(upload_to='photos/%y/%m/%d')

class Realestate(models.Model):
    tittle = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=3)
    space = models.CharField(max_length=60)
    description = models.CharField(max_length=120)
    location = models.CharField(max_length=50)
    Images = models.ImageField(upload_to='photos/%y/%m/%d')

class Jet(models.Model):
    brand = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    year = models.IntegerField(max_length=4)
    description = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=8, decimal_places=3)
    location = models.CharField(max_length=50)
    Images = models.ImageField(upload_to='photos/%y/%m/%d')

class Yacht(models.Model):
    brand = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    year = models.IntegerField(max_length=4)
    description = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=8, decimal_places=3)
    location = models.CharField(max_length=50)
    Images = models.ImageField(upload_to='photos/%y/%m/%d')


