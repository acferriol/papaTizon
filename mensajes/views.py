from django.shortcuts import render
from mensajes.models import Mensajes
from mensajes.filters import MensajeFilter1,MensajeFilter2
from mensajes.forms import MensajeForm
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import HttpResponseRedirect
from django_filters.views import FilterView
from django.views.generic import CreateView,DetailView,DeleteView
from django.urls import reverse_lazy

# Create your views here.
class RecibidosListView(UserPassesTestMixin,FilterView):
    model = Mensajes
    template_name = 'lista_mensajes_recibidos.html'
    filterset_class = MensajeFilter1

    def get_queryset(self):
        return self.model.objects.all().filter(destinatario=self.request.user) 
    
    def test_func(self):
        return self.request.user.is_authenticated

class EnviadosListView(UserPassesTestMixin,FilterView):
    model = Mensajes
    template_name = 'lista_mensajes_enviados.html'
    filterset_class = MensajeFilter2

    def get_queryset(self):
        return self.model.objects.all().filter(remitente=self.request.user) 
    
    def test_func(self):
        return self.request.user.is_authenticated


class MensajeCreate(UserPassesTestMixin,CreateView):
    model = Mensajes
    form_class = MensajeForm
    template_name = 'mensaje_crear.html'
    success_url = reverse_lazy('mensajes:mensajes_enviados')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST,request.FILES)
        #print(form)
        if form.is_valid():
            #print(request.POST)
            #print(form.cleaned_data)
            msj = form.save(commit=False)
            msj.remitente = request.user
            #msj.img = request.POST['img']
            msj.save()
            #print(msj)
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))

    def test_func(self):
        return self.request.user.is_authenticated

class MensajeDetalle(DetailView, UserPassesTestMixin): 
    model = Mensajes
    template_name = 'mensaje.html'

    def get(self, request, *args, **kwargs):
        id = kwargs['pk']
        msj = Mensajes.objects.get(pk=id)
        if msj.destinatario == request.user:
            msj.recibido = True
            msj.save()
        return super().get(request, *args, **kwargs)

    def test_func(self):
        return self.request.user.is_authenticated

