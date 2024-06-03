from rest_framework import  viewsets

from apps.products.models import Product
from apps.users.authentication_mixins import JWTAuthenticationMixin
from apps.products.api.serializer.product_serializer import ProductSerializer


class ProductViewSet(JWTAuthenticationMixin, viewsets.ViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    
