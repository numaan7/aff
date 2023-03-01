from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'link')
    
admin.site.register(Product, ProductAdmin)
