from django.contrib import admin
from apps.products.models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'category_product')

class MeasureUnitAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')
    
class CategoryProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')
    
class IndicatorAdmin(admin.ModelAdmin):
    list_display = ('id', 'descount_value', 'category_product')
    
class InventaryAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'measure_unit', 'quantity', 'price', 'category_product', 'indicator')

admin.site.register(MeasureUnit, MeasureUnitAdmin)
admin.site.register(CategoryProduct, CategoryProductAdmin)
admin.site.register(Indicator, IndicatorAdmin)
admin.site.register(Product)
admin.site.register(Inventary,InventaryAdmin )
