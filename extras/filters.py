import django_filters
from extras.models import DatosPlantacion
from empresa.models import Empresa
from django_filters import DateFromToRangeFilter
from django_filters.widgets import RangeWidget

class CultivarFilter(django_filters.FilterSet):
    empresa = django_filters.ModelChoiceFilter(
        field_name='empresa',
        queryset = Empresa.objects.all()
    )
    date_range = DateFromToRangeFilter(field_name='fecha',widget=RangeWidget(attrs={'placdholder':'YYYY/MM/DD','type':'date'}))
    def qs(self):
        parent = super().qs
        parent = parent.order_by("fecha").reverse()
        return parent