from django.db import models
from django.conf import settings
from apps.base.models import BaseModel

# Modelo Carrito
class Cart(BaseModel):
    
    # Campos
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Usuario')
    total = models.DecimalField('Total', max_digits=10, decimal_places=2, default=0)
    
    class Meta:
        verbose_name = 'Carrito'
        verbose_name_plural = 'Carritos'
        
    # Método para calcular el total del carrito
    def calculate_total(self):
        self.total = sum(item.subtotal for item in self.cartitem_set.all())
        self.save()
        
    # Método para agregar un producto al carrito
    def add_product(self, product, quantity):
        cart_item, created = CartItem.objects.get_or_create(cart=self, product=product, defaults={'quantity': quantity, 'price': product.price})
        if not created:
            cart_item.quantity += quantity
            cart_item.save()
        self.calculate_total()
        
    # Método para eliminar un producto del carrito
    def remove_product(self, product):
        cart_item = CartItem.objects.filter(cart=self, product=product).first()
        if cart_item:
            cart_item.delete()
            self.calculate_total()
            
    # Método para vaciar el carrito
    def clear(self):
        self.cartitem_set.all().delete()
        self.calculate_total()
        
    # Método para realizar el pago
    def pay(self):
        self.state = False
        self.save()
        
# Modelo Item de Carrito
class CartItem(BaseModel):
        
    # Campos
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name='Carrito')
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, verbose_name='Producto')
    quantity = models.PositiveIntegerField('Cantidad', default=1)
    price = models.DecimalField('Precio', max_digits=10, decimal_places=2)
    
    class Meta:
        verbose_name = 'Item de Carrito'
        verbose_name_plural = 'Items de Carrito'
            
    # Método para calcular el subtotal
    @property
    def subtotal(self):
        return self.quantity * self.price
