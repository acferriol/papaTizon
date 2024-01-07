from django.contrib import admin
from django.urls import path
from clima.views import ClimaCreate,ClimaList,ClimaUpdate,ClimaListToday,ResumenSemanal


urlpatterns = [
    path('lista_clima',ClimaList.as_view(),name="lista_clima"),
    path('lista_clima_hoy',ClimaListToday.as_view(),name="lista_clima_hoy"),
    path('crear_clima',ClimaCreate.as_view(),name="crear_clima"),
    path('editar_clima/<pk>/',ClimaUpdate.as_view(),name="editar_clima"),
    path('resumen_semanal',ResumenSemanal.as_view(),name="resumen_semanal")
]
