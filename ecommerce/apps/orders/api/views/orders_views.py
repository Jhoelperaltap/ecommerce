from rest_framework import viewsets
from apps.orders.models import Order
from apps.orders.api.serializer import order_serializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = order_serializer
