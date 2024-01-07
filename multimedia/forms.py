from dataclasses import fields
from xml.dom import ValidationErr
from django import forms
from empresa.models import Empresa
from django.contrib.admin import widgets
from django.core.exceptions import ValidationError

class GenForm(forms.Form):
    empresa = forms.ChoiceField(
        choices=[(emp.id,emp) for emp in Empresa.objects.all()],
        required=True,
        label="Empresa",
        widget= forms.Select(attrs={'class':'form-selected',"placeholder":"Empresa"})
    )
    fecha_inicio = forms.DateField(
        label = "Fecha Inicial",
        required=True,
        widget=forms.DateInput(attrs={'class':'form-control','type':'date'})
        
    )
    fecha_fin = forms.DateField(
        label = "Fecha Final",
        required=True,
        widget=forms.DateInput(attrs={'class':'form-control','type':'date'})
    )

    def clean_fecha_fin(self):
        i = self.cleaned_data['fecha_inicio']
        j = self.cleaned_data['fecha_fin']
        if i > j:
            raise ValidationError("Intoduzca fechas en orden cronológico")
        else:
            return j

    