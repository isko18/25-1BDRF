from rest_framework.generics import ListAPIView, CreateAPIView
from apps.product.models import Product, ProductImage
from apps.product.serializer import ProductSerializer, ProductImageSerializer

class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class ProductCreateAPIView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    