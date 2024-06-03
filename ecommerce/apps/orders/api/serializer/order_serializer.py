from rest_framework import serializers
from apps.orders.models import Order, OrderItem
from apps.customers.api.serializer.customers_serializers import CustomerSerializer
from apps.products.api.serializer.general_serializer import  MeasureUnitSerializer, CategoryProductSerializer
from apps.products.api.serializer.product_serializer import ProductSerializer

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    measure_unit = MeasureUnitSerializer(read_only=True)
    category_product = CategoryProductSerializer(read_only=True)
    
    class Meta:
        model = OrderItem
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    customer = CustomerSerializer(read_only=True)
    
    class Meta:
        model = Order
        fields = '__all__'
