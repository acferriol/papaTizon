from http.client import HTTPResponse
from django.views.generic import ListView,CreateView,UpdateView,TemplateView
from clima.models import Clima
from empresa.models import Empresa
from clima.forms import ClimaForm
from datetime import datetime, timedelta
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from django.shortcuts import HttpResponseRedirect
from clima.filters import ClimaFilter
from clima.utils import empresas_por_estacion,clasificar_dia,severidad,deteccion_inicial,buscar_senal,ultima_alerta,tipo_diagnostico
from django_filters.views import FilterView
# Create your views here.

class ClimaList(UserPassesTestMixin,FilterView):
    model = Clima
    template_name = 'clima_lista.html'
    filterset_class = ClimaFilter
    paginate_by = 7

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        parametros = self.request.GET.copy()
        #print('Antes del if',parametros)
        if parametros.get('page') != None:
            del parametros['page']
            #print(parametros)
        context['parametros'] = parametros 
        return context
    

    def test_func(self):
        return self.request.user.is_authenticated

class ClimaListToday(UserPassesTestMixin,ListView):
    model = Clima
    template_name = 'clima_lista_hoy.html'

    def get_queryset(self):
        return Clima.objects.all().filter(fecha=datetime.today().strftime('%Y-%m-%d'))

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_admin

class ClimaCreate(UserPassesTestMixin,CreateView):
    model = Clima
    form_class = ClimaForm
    template_name = 'clima_crear.html'
    success_url = reverse_lazy('clima:lista_clima_hoy')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tipo"] = tipo_diagnostico()
        return context

    #def post para clasificar dia
    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            clima = form.save(commit=False)
            clima.save()
            for emp in empresas_por_estacion(clima.estacion_id):
                clima.empresa.add(emp.id)
            clasificar_dia(clima.id)
            severidad(clima.id)
            deteccion_inicial(clima.id)
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))
        

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_admin

class ClimaUpdate(UserPassesTestMixin,UpdateView):
    model = Clima
    form_class = ClimaForm
    template_name = 'clima_crear.html'
    success_url = reverse_lazy('clima:lista_clima_hoy')

    #def post para clasificar dia
    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_clima = kwargs['pk']
        clima = self.model.objects.get(id = id_clima)
        form = self.form_class(request.POST,instance=clima)

        if form.is_valid():
            form.save()
            for emp in empresas_por_estacion(clima.estacion_id):
                clima.empresa.add(emp.id)
            clasificar_dia(clima.id)
            severidad(clima.id)
            deteccion_inicial(clima.id)
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_admin
      
class ResumenSemanal(TemplateView, UserPassesTestMixin):
    template_name = 'resumen_semanal.html'
    success_url = reverse_lazy('clima:resumen_semanal')
    datos = {}
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["empresas"] = Empresa.objects.all()
        if len(self.datos) > 0:
            context['datos'] = self.datos
        return context
    
    def get(self, request, *args, **kwargs):
        defEmp = request.user.empresa.nombre
        idEmp = request.user.empresa.id
        defEnd = datetime.today()
        #print(defEnd)
        defStart = defEnd - timedelta(days=6)
        week = Clima.objects.all().filter(empresa=idEmp).filter(fecha__gte=defStart).filter(fecha__lte=defEnd)
        num_days = len(week)
        sev_acum = 0
        favs = 0
        det_inic = 0
        for day in week:
            if day.severidad > -1:
                sev_acum+=day.severidad
            if day.favorable == 1:
                favs+=1
            if day.deteccion_inicial > 0:
                det_inic = max(det_inic, day.deteccion_inicial)
        senal = buscar_senal(sev_acum,favs)
        ult_alerta = ultima_alerta(idEmp)
        self.datos = {'empresa':defEmp,'dias':num_days,'severidad':sev_acum,'dias_favorables':favs, 'deteccion':det_inic, 'alerta':senal,'ult_alerta':ult_alerta,
            'start':defStart,'end':defEnd
        }
        return self.render_to_response(self.get_context_data())
    
    def post(self, request, *args, **kwargs):
        seleccion = self.request.POST['empresa']
        end = self.request.POST['fecha']
        end = datetime.strptime(end, '%Y-%m-%d')
        print(end)
        start = end - timedelta(days=6)
        if seleccion != 'Seleccionar una empresa':
            emp = int(seleccion)
            nomb_emp = Empresa.objects.values('nombre').filter(id=emp)
            nomb_emp = nomb_emp[0]['nombre']
            week = Clima.objects.all().filter(empresa=emp).filter(fecha__gte=start).filter(fecha__lte=end)
            num_days = len(week)
            sev_acum = 0
            favs = 0
            det_inic = 0
            for day in week:
                if day.severidad > -1:
                    sev_acum+=day.severidad
                if day.favorable == 1:
                    favs+=1
                if day.deteccion_inicial > 0:
                    det_inic = max(det_inic, day.deteccion_inicial)
            senal = buscar_senal(sev_acum,favs)
            ult_alerta = ultima_alerta(emp)
            self.datos = {'empresa':nomb_emp,'dias':num_days,'severidad':sev_acum,'dias_favorables':favs, 'deteccion':det_inic, 'alerta':senal,'alerta':senal,'ult_alerta':ult_alerta, 'start':start,'end':end}
           
        return self.render_to_response(self.get_context_data())

    def test_func(self):
        return self.request.user.is_authenticated
            
    

    
    
    
