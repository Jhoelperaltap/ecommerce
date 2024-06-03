from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.customers.api.views.customers_views import CustomerViewSet

router = DefaultRouter()
router.register(r'customers', CustomerViewSet, basename='customers')


urlpatterns = router.urls