from rest_framework import serializers
from apps.product.models import Product, ProductImage

class ProductImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    
    class Meta:
        model = ProductImage
        fields = ['image', 'position']
        
class ProductSerializer(serializers.ModelSerializer):
    product_image = ProductImageSerializer(many=True, read_only=True)
    
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'is_active', 'product_image', 'created_at']
        