from django.shortcuts import render
from extras.models import Aparicion, DatosPlantacion
from django.contrib.auth.mixins import UserPassesTestMixin
from django_filters.views import FilterView
from extras.filters import CultivarFilter
from extras.forms import PlantacionForm,AparicionForm
from django.views.generic import ListView,CreateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.
class PorcentajeListView(UserPassesTestMixin,FilterView):
    model = DatosPlantacion
    template_name = 'datos_plantacion.html'
    filterset_class = CultivarFilter

    def test_func(self):
        return self.request.user.is_authenticated

class PorcentajeCreateView(UserPassesTestMixin,CreateView):
    model = DatosPlantacion
    form_class = PlantacionForm
    template_name = 'crear_plantacion.html'
    success_url = reverse_lazy('extras:porcentaje_list')

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_admin

class PorcentajeDelete(UserPassesTestMixin,DeleteView):
    model = DatosPlantacion
    template_name = 'plantacion_delete.html'
    success_url = reverse_lazy('extras:porcentaje_list')

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_admin

class AparicionListView(UserPassesTestMixin,FilterView):
    model = Aparicion
    template_name = 'datos_deteccion.html'
    filterset_class = CultivarFilter

    def test_func(self):
        return self.request.user.is_authenticated

class AparicionView(UserPassesTestMixin,CreateView):
    model = Aparicion
    form_class = AparicionForm
    template_name = 'ingresar_deteccion.html'
    success_url = reverse_lazy('extras:aparicion_list')

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_admin

class AparicionDelete(UserPassesTestMixin,DeleteView):
    model = Aparicion
    template_name = 'aparicion_delete.html'
    success_url = reverse_lazy('extras:aparicion_list')

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_admin