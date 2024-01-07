from pyexpat import model
from django import forms
from empresa.models import Empresa
from estacion.models import Estacion
from clima.models import Clima

class ClimaForm(forms.ModelForm):
    
    class Meta:
        model = Clima

        fields = [
            'fecha',
            'estacion',
            'temperatura_media',
            'temperatura_maxima',
            'temperatura_minima',
            'precipitacion',
            'horas_hr_90',
            'temperatura_media_hr_90',
        ]

        labels = {
            'fecha':'Fecha de Hoy',
            'estacion':'Código de la estación',
            'temperatura_media': 'Temperatura media',
            'temperatura_maxima':'Temperatura máxima',
            'temperatura_minima':'Temperatura mínima',
            'precipitacion':'Precipitaciones (mm)',
            'horas_hr_90':'Horas HR >= 90%',
            'temperatura_media_hr_90': 'T med. (HR >= 90%) ',
        }

        widgets = {
            'fecha': forms.DateInput(attrs={'class':'form-control','type':'date'},format="%Y-%m-%d"),
            'estacion': forms.Select(attrs={'class':'form-control','aria-label':'Numero de estacion','placeholder':'Num. de estación'}),
            'temperatura_media': forms.NumberInput(attrs={'class':'form-control','placeholder':'Temp. med'}),
            'temperatura_maxima':forms.NumberInput(attrs={'class':'form-control','placeholder':'Temp. max'}),
            'temperatura_minima':forms.NumberInput(attrs={'class':'form-control','placeholder':'Temp. min'}),
            'precipitacion':forms.NumberInput(attrs={'class':'form-control','placeholder':'Precipitaciones'}),
            'horas_hr_90':forms.NumberInput(attrs={'class':'form-control','placeholder':'Horas (HR >= 90%)'}),
            'temperatura_media_hr_90': forms.NumberInput(attrs={'class':'form-control','placeholder':'Temp. Media (HR >=90%)'}),
        }

        

