from django.contrib import admin
from .models import Products

# Register your models here.

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    list_filter = ('created_at', 'updated_at')

    

admin.site.register(Products)



