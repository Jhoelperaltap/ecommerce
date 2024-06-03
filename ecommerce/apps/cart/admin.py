from django.contrib import admin
from apps.cart.models import *

class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total')
    
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'cart', 'product', 'quantity', 'price')
    
admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)

