from django.db import models
from datetime import datetime
from estacion.models import Estacion
from empresa.models import Empresa

# Create your models here.

class Clima(models.Model):
    class Meta:
        unique_together = (('fecha','estacion'),)

    fecha = models.DateField(default=datetime.today().strftime('%Y-%m-%d'))
    estacion = models.ForeignKey(Estacion, null = False, blank=False, on_delete = models.CASCADE)
    temperatura_media = models.DecimalField(decimal_places=1,max_digits=5, null=True, blank=True)
    temperatura_maxima = models.DecimalField(decimal_places=1,max_digits=5, null=True, blank=True)
    temperatura_minima = models.DecimalField(decimal_places=1,max_digits=5, null=True,blank=True)
    precipitacion = models.DecimalField(decimal_places=1,max_digits=5, null=True,blank=True)
    horas_hr_90 = models.DecimalField(decimal_places=1,max_digits=5, null=True,blank=True)
    temperatura_media_hr_90 = models.DecimalField(decimal_places=1,max_digits=5, null=True,blank=True)
    empresa = models.ManyToManyField(Empresa)
    favorable = models.IntegerField(null=True) # -1 no determinable
    severidad = models.IntegerField(null=True) # -1 no determinable
    deteccion_inicial = models.IntegerField(null=True)