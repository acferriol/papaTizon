from django.db import models
from empresa.models import Empresa
from datetime import datetime
# Create your models here.

class Aparicion(models.Model):
    class Meta:
        unique_together = (('fecha','empresa'),)
    empresa = models.ForeignKey(Empresa, null = False, blank=False, on_delete = models.CASCADE)
    fecha =  models.DateField(default=datetime.today().strftime('%Y-%m-%d'))


class DatosPlantacion(models.Model):
    empresa = models.ForeignKey(Empresa, null = False, blank=False, on_delete = models.CASCADE)
    cultivar = models.CharField(max_length=30)
    fecha =  models.DateField(default=datetime.today().strftime('%Y-%m-%d'),null=False)
    porcentaje = models.DecimalField(decimal_places=2,max_digits=5, null=False)