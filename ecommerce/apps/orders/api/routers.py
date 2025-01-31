from rest_framework.routers import DefaultRouter
from apps.orders.api.views.orders_views import OrderViewSet


router = DefaultRouter()

router.register(r'orders', OrderViewSet, basename= 'orders')

urlpatterns = router.urls