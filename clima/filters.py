from cgitb import lookup
import django_filters
from clima.models import Clima
from empresa.models import Empresa
from django_filters import DateFilter,DateFromToRangeFilter
from django_filters.widgets import RangeWidget

class ClimaFilter(django_filters.FilterSet):

    empresa = django_filters.ModelChoiceFilter(
        field_name='empresa',
        queryset = Empresa.objects.all()
    )
    date_range = DateFromToRangeFilter(field_name='fecha',widget=RangeWidget(attrs={'placdholder':'YYYY/MM/DD','type':'date'}))
    @property
    def qs(self):
        parent = super().qs
        parent = parent.values("fecha","estacion","empresa__nombre",'temperatura_media',
            'temperatura_maxima',
            'temperatura_minima',
            'precipitacion',
            'horas_hr_90',
            'temperatura_media_hr_90','favorable','severidad','deteccion_inicial').order_by("fecha").reverse()
        return parent

