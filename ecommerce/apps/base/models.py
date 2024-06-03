from django.db import models
from django.utils import timezone

# Modelo Base
class BaseModel(models.Model):
    
    id = models.AutoField(primary_key=True)  
    state = models.BooleanField('Estado', default=True) 
    created_date = models.DateTimeField('Fecha de Creación',auto_now= False, auto_now_add=True)
    modified_date = models.DateTimeField('Fecha de Modificación',auto_now=True, auto_now_add= False)
    deleted_date = models.DateTimeField('Fecha de Eliminación',auto_now=True, auto_now_add=False)
    
    class Meta:
        # Indicamos que es una clase abstracta
        abstract = True
        verbose_name = 'Modelo Base'
        verbose_name_plural = 'Modelos Base'
        
    # Método para marcar un registro como eliminado
    def delete(self, using=None, keep_parents=False):
        self.state = False
        self.deleted_date = timezone.now()
        self.save()

    # Método para restaurar un registro eliminado
    def restore(self):
        self.state = True
        self.deleted_date = None
        self.save()

