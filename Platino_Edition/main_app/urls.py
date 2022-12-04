from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('home/', views.home, name='home'),
    path('yachts/', views.yachts, name='yachts'),
    path('jets/', views.jets, name='jets'),
    path('realstates/', views.realstates, name='realstates'),
    path('car/', views.car, name='car'),

]
