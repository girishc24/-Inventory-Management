from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('adduser/', views.adduser, name='adduser'),
    path('items/', views.ItemDetailView.as_view(), name='item_detail'),
    path('items/<int:item_id>/', views.ItemDetailView.as_view(), name='item_detail'),

   
]