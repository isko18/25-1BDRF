# from rest_framework.generics import ListAPIView, CreateAPIView,RetrieveAPIView, UpdateAPIView, DestroyAPIView

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from apps.product.models import Product
from apps.product.serializer import ProductSerializer
from apps.product.utils import ProductPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

class ProductMixins(GenericViewSet,
                    mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.DestroyModelMixin):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = ("slug")
    pagination_class = ProductPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    
    search_fields = ['title', 'description']
    ordering_fields = ['price', 'created_at']
    ordering = ['-created_at']
    


# class ProductListAPIView(ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
    
# class ProductCreateAPIView(CreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
    
# class ProductRetrieveAPIView(RetrieveAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     lookup_field = ('slug')
    
# class ProductUpdateAPIView(UpdateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
    
# class ProductDestroyAPIView(DestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
    