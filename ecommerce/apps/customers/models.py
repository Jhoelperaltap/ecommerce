from django.db import models
from django.conf import settings
from simple_history.models import HistoricalRecords
from apps.base.models import BaseModel

class Customer(BaseModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Usuario', null=False)
    first_name = models.CharField('Nombre', max_length=50, null=False)
    last_name = models.CharField('Apellido', max_length=50, null=False)
    phone = models.CharField('Teléfono', max_length=20, null=True, blank=True)
    address = models.CharField('Dirección', max_length=255, null=False)
    city = models.CharField('Ciudad', max_length=100, null=False)
    postal_code = models.CharField('Código Postal', max_length=20, null=True, blank=True)
    country = models.CharField('País', max_length=50, null=False)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.Changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.Changed_by = value

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.user.username})'
