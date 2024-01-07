from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from estacion.models import Estacion
from estacion.forms import EstacionForm
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
# Create your views here.

class EstacionList(UserPassesTestMixin,ListView):
    model = Estacion
    template_name = 'estacion_lista.html'

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_admin

class EstacionCreate(UserPassesTestMixin,CreateView):
    model = Estacion
    form_class = EstacionForm
    template_name = 'estacion_crear.html'
    success_url = reverse_lazy('estacion:lista_estacion')

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_admin

class EstacionDelete(UserPassesTestMixin,DeleteView):
    model = Estacion
    template_name = 'estacion_delete.html'
    success_url = reverse_lazy('estacion:lista_estacion')

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_admin

class EstacionUpdate(UserPassesTestMixin,UpdateView):
    model = Estacion
    form_class = EstacionForm
    template_name = 'estacion_crear.html'
    success_url = reverse_lazy('estacion:lista_estacion')

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_admin
      