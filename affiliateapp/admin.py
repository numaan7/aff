from django.contrib import admin
from .models import Product, Blog

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'link')
    
admin.site.register(Product, ProductAdmin)

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    
admin.site.register(Blog, BlogAdmin)
