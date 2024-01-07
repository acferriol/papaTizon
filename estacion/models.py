from django.db import models

# Create your models here.

class Estacion(models.Model):
    num_estacion = models.CharField(max_length=6, primary_key=True)
    nombre = models.CharField(max_length=50)
    provincia = models.CharField(max_length=30)

    def __str__(self):
        return '{} {}'.format(self.num_estacion,self.nombre)