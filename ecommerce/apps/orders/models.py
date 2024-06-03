from django.db import models
from simple_history.models import HistoricalRecords
from apps.base.models import BaseModel
from apps.customers.models import Customer  # Importamos el modelo Customer
from apps.products.models import Product, MeasureUnit, CategoryProduct

class Order(BaseModel):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Cliente', null=False)
    total_amount = models.DecimalField('Monto Total', max_digits=10, decimal_places=2)
    status = models.CharField('Estado', max_length=50, choices=[
        ('pending', 'Pendiente'),
        ('processing', 'En Proceso'),
        ('shipped', 'Enviado'),
        ('delivered', 'Entregado'),
        ('canceled', 'Cancelado')
    ])
    historical = HistoricalRecords()

    class Meta:
        verbose_name = 'Orden'
        verbose_name_plural = 'Órdenes'
        
    def __str__(self):
        return f'Order {self.id} - Customer {self.customer.user.username} - {self.total_amount}'

class OrderItem(BaseModel):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField('Cantidad', default=1)
    price = models.DecimalField('Precio', max_digits=10, decimal_places=2)
    measure_unit = models.ForeignKey(MeasureUnit, on_delete=models.CASCADE, verbose_name='Unidad de Medida', null=True)
    category_product = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, verbose_name='Categoría de Producto', null=True)
    historical = HistoricalRecords()

    class Meta:
        verbose_name = 'Item de Orden'
        verbose_name_plural = 'Items de Órdenes'
        
    def __str__(self):
        return f'{self.product.name} - {self.quantity} x {self.price}'
