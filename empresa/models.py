from unittest.util import _MAX_LENGTH
from django.db import models
from estacion.models import Estacion
# Create your models here.

class Empresa(models.Model):
    nombre = models.CharField(max_length=60)
    estacion = models.ForeignKey(Estacion, null = True, blank=False, on_delete = models.CASCADE)
    representante = models.CharField(max_length = 100)
    municipio = models.CharField(max_length = 100)
    provincia = models.CharField(max_length=30)

    def __str__(self):
        return '{}'.format(self.nombre)