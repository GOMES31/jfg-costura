from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'), 
    path('about/', views.about, name = 'about'),
    path('shop/', views.shop, name = 'shop'), 
    path('machine/<slug:slug>/', views.machine_detail, name='machine_detail'),
    path('contact/', views.contact, name = 'contact'), 
]