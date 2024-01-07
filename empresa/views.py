from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from empresa.models import Empresa
from empresa.forms import EmpresaForm
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
# Create your views here.

class EmpresaList(UserPassesTestMixin,ListView):
    model = Empresa
    template_name = 'empresa_lista.html'

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_admin

class EmpresaCreate(UserPassesTestMixin,CreateView):
    model = Empresa
    form_class = EmpresaForm
    template_name = 'empresa_crear.html'
    success_url = reverse_lazy('empresa:lista_empresa')

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_admin

class EmpresaDelete(UserPassesTestMixin,DeleteView):
    model = Empresa
    template_name = 'empresa_delete.html'
    success_url = reverse_lazy('empresa:lista_empresa')

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_admin

class EmpresaUpdate(UserPassesTestMixin,UpdateView):
    model = Empresa
    form_class = EmpresaForm
    template_name = 'empresa_crear.html'
    success_url = reverse_lazy('empresa:lista_empresa')

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_admin
      