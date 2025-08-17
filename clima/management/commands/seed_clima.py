from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import datetime, timedelta
from random import randint, choice, uniform

from clima.models import Clima, Estacion, Empresa
from clima.utils import (
    severidad,
    clasificar_dia,
    deteccion_inicial,
    empresas_por_estacion,
)

# Definimos variedades
TVARIEDAD = (
    ("erecto", "erecto"),
    ("rastrero", "rastrero"),
    ("arrosetada", "arrosetada"),
)


class Command(BaseCommand):
    help = "Seed de datos para Clima, Estacion y Empresa"

    def handle(self, *args, **options):
        # Crear estaciones si no existen
        estaciones = []
        for i in range(1, 4):
            num_estacion = f"EST{i:02d}"
            estacion, created = Estacion.objects.get_or_create(
                num_estacion=num_estacion,
                defaults={
                    "nombre": f"Estación {i}",
                    "provincia": choice(
                        ["La Habana", "Pinar del Río", "Camagüey", "Santiago de Cuba"]
                    ),
                },
            )
            if created:
                self.stdout.write(f"✅ Estación creada: {estacion}")
            else:
                self.stdout.write(f"🔁 Estación existente: {estacion}")
            estaciones.append(estacion)

        # Crear empresas si no existen
        empresas = []
        for i in range(1, 6):
            empresa, created = Empresa.objects.get_or_create(
                nombre=f"Empresa {i}",
                defaults={
                    "estacion": estaciones[i % 3],
                    "representante": f"Rep {i}",
                    "municipio": f"Municipio {i}",
                    "provincia": "La Habana",
                    "variedad_actual": choice(TVARIEDAD)[0],
                },
            )
            if created:
                self.stdout.write(f"✅ Empresa creada: {empresa}")
            else:
                self.stdout.write(f"🔁 Empresa existente: {empresa}")
            empresas.append(empresa)

        # Fechas: los últimos 30 días
        today = timezone.now().date()
        fechas = [today - timedelta(days=x) for x in range(30, 0, -1)]

        # Generar datos de clima
        clima_count = 0
        for estacion in estaciones:
            for fecha in fechas:
                # Evitar duplicados por (fecha, estacion)
                if Clima.objects.filter(fecha=fecha, estacion=estacion).exists():
                    continue

                clima = Clima.objects.create(
                    fecha=fecha,
                    estacion=estacion,
                    temperatura_media=round(uniform(18.0, 25.0), 1),
                    temperatura_maxima=round(uniform(24.0, 30.0), 1),
                    temperatura_minima=round(uniform(10.0, 22.0), 1),
                    precipitacion=(
                        round(uniform(4.0, 20.0), 1) if randint(0, 1) else 5.0
                    ),
                    horas_hr_90=round(uniform(0.0, 24.0), 1) if randint(0, 1) else 9,
                    temperatura_media_hr_90=(
                        round(uniform(10.0, 30.0), 1) if randint(0, 1) else 11
                    ),
                )

                # Asociar empresas aleatorias al clima
                for emp in empresas_por_estacion(clima.estacion_id):
                    clima.empresa.add(emp.id)
                clima.save()

                id_clima = clima.id
                clasificar_dia(id_clima)
                severidad(id_clima)
                deteccion_inicial(id_clima)

                clima_count += 1
                self.stdout.write(f"🌤️ Clima creado: {fecha} - {estacion}")

        self.stdout.write(
            self.style.SUCCESS(f"Se crearon {clima_count} registros de Clima.")
        )
