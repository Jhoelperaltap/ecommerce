from django.db import models
from simple_history.models import HistoricalRecords

from apps.base.models import BaseModel

# Modelo para las unidades de medida de los productos
class MeasureUnit(BaseModel):
    description = models.CharField('Descripción', max_length=50, unique=True, blank=False, null=False)
    historical = HistoricalRecords()
    
    @property
    def _history_user(self):
        return self.Changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.Changed_by = value
        
    class Meta:
        verbose_name = 'Unidad de Medida'
        verbose_name_plural = 'Unidades de Medida'
        
    def __str__(self):
        return self.description

# Modelo para las categorías de productos
class CategoryProduct(BaseModel):
    description = models.CharField('Descripción', max_length=50, unique=True, blank=False, null=False)
    historical = HistoricalRecords()
    
    @property
    def _history_user(self):
        return self.Changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.Changed_by = value
        
    class Meta:
        verbose_name = 'Categoria de Producto'
        verbose_name_plural = 'Categorias de Productos'
        
    def __str__(self):
        return self.description

# Modelo para los indicadores de ofertas
class Indicator(BaseModel):
    descount_value = models.PositiveSmallIntegerField('Valor de Descuento', default=0)
    category_product = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, verbose_name='Indicador de Ofertas')
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.Changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.Changed_by = value
        
    class Meta:
        verbose_name = 'Indicador de Oferta'
        verbose_name_plural = 'Indicadores de Ofertas'
        
    def __str__(self):
        return f'Oferta de la categoría {self.category_product}: {self.descount_value}%'

# Modelo para los productos
class Product(BaseModel):
    name = models.CharField('Nombre de Producto', max_length=150, unique=True, blank=False, null=False)
    description = models.TextField('Descripción de Producto', blank=False, null=False)
    image = models.ImageField('Imagen del Producto', upload_to='products/', blank=True, null=True)
    measure_unit = models.ForeignKey(MeasureUnit, on_delete=models.CASCADE, verbose_name='Unidad de Medida', null=True)
    category_product = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, verbose_name='Categoría de Producto', null=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.Changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.Changed_by = value
        
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        
    def __str__(self):
        return self.name

class Inventary(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Producto', null=False)
    quantity = models.PositiveIntegerField('Cantidad', default=0)
    measure_unit = models.ForeignKey(MeasureUnit, on_delete=models.CASCADE,
    verbose_name='Unidad de Medida', null=True)
    price = models.DecimalField('Precio', max_digits=10, decimal_places=2, null=True)  # Ejemplo de campo agregado
    category_product = models.ForeignKey(CategoryProduct, on_delete=models.
    CASCADE, verbose_name='Categoría de Producto', null=True)  # Ejemplo de campo agregado
    indicator = models.BooleanField('Indicador', default=False)  # Ejemplo de campo agregado
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.Changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.Changed_by = value

    class Meta:
        verbose_name = 'Inventario'
        verbose_name_plural = 'Inventarios'
        
    def __str__(self):
        return f'{self.product} - {self.quantity}'