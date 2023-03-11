from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('products', views.products),
    path('about/', views.about),
    path('services', views.services),

    path('client', views.client),
    path('contact', views.contact),
    path('blogs', views.blogs),

    path('blog/<str:posttitle>/', views.blogbytitle),
    path('service/<str:servicetitle>/', views.servicebytitle),

    path('submitform/', views.submitform),
    path('writeforus/', views.write),
    path('sitemap/', views.sitemap),




]
