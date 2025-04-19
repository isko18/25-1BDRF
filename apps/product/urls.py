from django.urls import path
from apps.product.views import ProductListAPIView

urlpatterns = [
    path('product_list/', ProductListAPIView.as_view(), name="list")
]
