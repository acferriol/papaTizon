from django import forms
from extras.models import DatosPlantacion, Aparicion
from empresa.models import Empresa

class PlantacionForm(forms.ModelForm):
    cultivar = forms.CharField(
        label = "Cultivar",
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"Cultivar"
            }
        )
    )
    porcentaje = forms.DecimalField(
        label = "Porcentaje",
        widget= forms.NumberInput(
            attrs={
                "class":"form-control",
                "placeholder":"Porcentaje"
            }
        )
    )

    class Meta:
        model = DatosPlantacion
        fields = ('empresa', 'cultivar','fecha','porcentaje')
        labels = {'fecha':'Fecha','empresa':'Empresa'}
        widgets = {'fecha':forms.DateInput(attrs={'class':'form-control','type':'date'},format="%Y-%m-%d")}


class AparicionForm(forms.ModelForm):
    class Meta:
        model = Aparicion
        fields = ('empresa','fecha')
        labels = {'fecha':'Fecha','empresa':'Empresa'}
        widgets = {'fecha':forms.DateInput(attrs={'class':'form-control','type':'date'},format="%Y-%m-%d")}