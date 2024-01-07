import django_filters
from mensajes.models import Mensajes
from users.models import User

class MensajeFilter1(django_filters.FilterSet):
    remitente = django_filters.ModelChoiceFilter(
        field_name='remitente',
        queryset = User.objects.all()
    )
    recibido = django_filters.BooleanFilter()
    def qs(self):
        parent = super().qs
        parent = parent.order_by("created_at").reverse()
        return parent

class MensajeFilter2(django_filters.FilterSet):
    destinatario = django_filters.ModelChoiceFilter(
        field_name='destinatario',
        queryset = User.objects.all()
    )
    recibido = django_filters.BooleanFilter()
    def qs(self):
        parent = super().qs
        parent = parent.order_by("created_at").reverse()
        return parent