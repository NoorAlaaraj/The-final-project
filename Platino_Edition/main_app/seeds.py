from .models import *


data = [
    { name='', wheels=''},
    { name='', wheels=''},
    { name='', wheels=''},
    { name='', wheels=''},
    { name='', wheels=''},
]



for obj in data:
    Wheels.objects.create(obj)

