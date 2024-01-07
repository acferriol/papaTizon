from django.contrib import admin
from django.urls import path
from estacion.views import EstacionCreate,EstacionList,EstacionDelete,EstacionUpdate
from django.contrib.auth.decorators import user_passes_test


urlpatterns = [
    path('lista_estaciones',EstacionList.as_view(),name="lista_estacion"),
    path('crear_estacion',EstacionCreate.as_view(),name="crear_estacion"),
    path('eliminar_estacion/<pk>/',EstacionDelete.as_view(),name="eliminar_estacion"),
    path('editar_estacion/<pk>/',EstacionUpdate.as_view(),name="editar_estacion")
]
