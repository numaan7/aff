from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('products', views.products),
    path('about', views.about),
    path('client', views.client),
    path('contact', views.contact),
    path('blog/<str:posttitle>/', views.blogbytitle),

]
