from rest_framework.routers import DefaultRouter
from apps.products.api.views.general_views import MeasureUniViewSet, CategoryProductViewSet, IndicatorViewSet, InventarySerializerViewSet
from apps.products.api.views.product_viewsets import ProductViewSet

router = DefaultRouter()

router.register(r'measure-unit', MeasureUniViewSet, basename='measure_unit')
router.register(r'category-product', CategoryProductViewSet, basename='category_products')
router.register(r'indicator', IndicatorViewSet, basename='indicators')
router.register(r'inventary', InventarySerializerViewSet, basename='inventary')
router.register(r'product', ProductViewSet, basename='product')

urlpatterns = router.urls