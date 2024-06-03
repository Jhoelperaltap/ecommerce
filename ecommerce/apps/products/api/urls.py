from django.urls import path
from apps.products.api.views.general_views import MeasureUniViewSet, CategoryProductViewSet, IndicatorViewSet, InventarySerializerViewSet

urlpatterns = [
    path('measure-unit/', MeasureUniViewSet.as_view(), name='measure_unit'),
    path('measure-unit/<int:pk>/', MeasureUniViewSet.as_view(), name='measure_unit'),
    path('category-product/', CategoryProductViewSet.as_view(), name='category_products'),
    path('category-product/<int:pk>/', CategoryProductViewSet.as_view(), name='category_products'),
    path('indicator/', IndicatorViewSet.as_view(), name='indicators'),
    path('indicator/<int:pk>/', IndicatorViewSet.as_view(), name='indicators'),
    path('inventary/', InventarySerializerViewSet.as_view()),
    path('inventary/<int:pk>/', InventarySerializerViewSet.as_view(), name='inventary'),
]