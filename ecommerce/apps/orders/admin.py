from django.contrib import admin
from apps.orders.models import *

admin.site.register(Order)
admin.site.register(OrderItem)


