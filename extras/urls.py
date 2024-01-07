from django.urls import path
from extras.views import AparicionView,PorcentajeCreateView,PorcentajeListView,AparicionListView,AparicionDelete,PorcentajeDelete

urlpatterns = [
    path('aparicion',AparicionView.as_view() ,name="aparicion"),
    path('aparicion_delete/<pk>/',AparicionDelete.as_view() ,name="aparicion_delete"),
    path('aparicion_list',AparicionListView.as_view() ,name="aparicion_list"),
    path('porcentaje',PorcentajeCreateView.as_view() ,name="porcentaje"),
    path('porcentaje_delete/<pk>/',PorcentajeDelete.as_view() ,name="porcentaje_delete"),
    path('porcentaje_list',PorcentajeListView.as_view() ,name="porcentaje_list"),
]
