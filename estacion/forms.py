from dataclasses import fields
from django import forms
from estacion.models import Estacion

class EstacionForm(forms.ModelForm):
    num_estacion = forms.CharField(
        label = "Estacion",
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"Estacion"
            }
        )
    )
    nombre = forms.CharField(
        label = "Nombre",
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"Nombre"
            }
        )
    )
    PROVINCIAS = (
        ("Pinar del Rio","Pinar del Rio"),
        ("La Habana","La Habana"),
        ("Artemisa","Artemisa"),
        ("Mayabeque","Mayabeque"),
        ("Isla de la Juventud","Isla de la Juventud"),
        ("Matanzas","Matanzas"),
        ("Villa Clara","Villa Clara"),
        ("Cienfuegos","Cienfuegos"),
        ("Ciego de Avila","Ciego de Avila"),
        ("Sancti Spiritus","Sancti Spiritus"),
        ("Camaguey","Camaguey"),
        ("Las Tunas","Las Tunas"),
        ("Holguin","Holguin"),
        ("Granma","Granma"),
        ("Santiago de Cuba","Santiago de Cuba"),
        ("Guantanamo","Guantanamo")
    )

    provincia = forms.ChoiceField(
        label = "Provincia",
        choices=PROVINCIAS,
        widget=forms.Select(
            attrs={
                "class":"form-select",
                "placeholder":"Provincia",
            }
        )
    )
    


    class Meta:
        model = Estacion
        fields = ('num_estacion', 'nombre','provincia')
        
            
