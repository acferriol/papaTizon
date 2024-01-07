from django import forms
from mensajes.models import Mensajes

class MensajeForm(forms.ModelForm):  

    class Meta:
        model = Mensajes
        fields = (
            'destinatario',
            'tipodemensaje',
            'tipodealerta',
            'mensaje',
            'img'
        )
        labels = {
           'destinatario':'Destinatario',
           'tipodemensaje':'Tipo de Mensaje',
           'tipodealerta': 'Tipo de Alerta',
           'mensaje':'Texto',
           'img':'Adjunto' 
        }
        widgets = {
            'destinatario':forms.Select(attrs={'class':'form-control'}),
            'tipodemensaje':forms.Select(attrs={'class':'form-control'}),
            'tipodealerta':forms.Select(attrs={'class':'form-control'}),
            'mensaje':forms.Textarea(attrs={'class':'form-control','style':'width:100%'})
        }
        
            