from rest_framework import viewsets
from apps.products.models import *
from apps.products.api.serializer.general_serializer import MeasureUnitSerializer, CategoryProductSerializer, IndicatorSerializer, InventarySerializer


class MeasureUniViewSet(viewsets.ModelViewSet):
    queryset = MeasureUnit.objects.all()
    serializer_class = MeasureUnitSerializer
    

class IndicatorViewSet(viewsets.ModelViewSet):
    queryset = Indicator.objects.all()
    serializer_class = IndicatorSerializer
    
    
class CategoryProductViewSet(viewsets.ModelViewSet):
    queryset = CategoryProduct.objects.all()
    serializer_class = CategoryProductSerializer
    
class InventarySerializerViewSet(viewsets.ModelViewSet):
    queryset = Inventary.objects.all()
    serializer_class = InventarySerializer
    