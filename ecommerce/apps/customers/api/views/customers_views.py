from rest_framework import viewsets
from apps.customers.models import Customer
from apps.customers.api.serializer import customers_serializers

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = customers_serializers
