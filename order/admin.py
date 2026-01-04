from django.contrib import admin
from .models import Order, OrderItem
# Register your models here.

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'status', 'created_at', 'updated_at')
    search_fields = ('customer__username', 'status')
    list_filter = ('status', 'created_at')
    ordering = ('-created_at',)

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'quantity', 'price')
    search_fields = ('order__id', 'product__name')
    list_filter = ('product',)
    ordering = ('-order__created_at',)
