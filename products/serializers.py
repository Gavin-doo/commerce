from rest_framework_simplejwt import serializers
from .models import Products

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'name', 'description', 'price', 'stock', 'created_at', 'updated_at']