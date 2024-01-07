from django.contrib import admin
from django.urls import path
from mensajes.views import MensajeCreate,MensajeDetalle,RecibidosListView,EnviadosListView


urlpatterns = [
    path('mensajes_recibidos',RecibidosListView.as_view(),name="mensajes_recibidos"),
    path('mensajes_enviados',EnviadosListView.as_view(),name="mensajes_enviados"),
    path('mensaje_detalle/<pk>/',MensajeDetalle.as_view(),name="mensaje_detalle"),
    path('redactar_mensaje',MensajeCreate.as_view(),name="redactar_mensaje")
]