from django import forms
from empresa.models import Empresa
from estacion.models import Estacion


class EmpresaForm(forms.ModelForm):

    nombre = forms.CharField(
        label = "Nombre",
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"Nombre"
            }
        )
    )
    representante = forms.CharField(
        label = "Representante",
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"Persona Representante"
            }
        )
    )
    municipio = forms.CharField(
        label = "Municipio",
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"Municipio"
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
        model = Empresa
        fields = ('nombre','estacion','representante','municipio' ,'provincia')
        labels = {'estacion':"Estacion"}
        widgets = {'estacion':forms.Select(attrs={'class':'form-control'})}
        
            
