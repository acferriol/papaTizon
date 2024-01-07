from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import User, SEXO
from empresa.models import Empresa

class LoginForm(forms.Form):
    username = forms.CharField(
        label = "Usuario",
        widget=forms.TextInput(
            attrs={
                "class":"form-control" 
            }
        )
    )
    password = forms.CharField(
        label = "Password",
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control" 
            }
        )
    )


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        label = "Usuario",
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"Usuario"
            }
        )
    )
    password1 = forms.CharField(
        label = "Password",
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder":"Contraseña"
            }
        )
    )
    password2 = forms.CharField(
        label = "Confirmar Password",
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder":"Confirmar contraseña"
            }
        )
    )
    email = forms.EmailField(
        widget = forms.EmailInput(
            attrs={
                "class":"form-control",
                "placeholder":"Email"
            }
        )
    )
    first_name = forms.CharField(
        label = "Nombre",
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"Nombre"
            }
        )
    )
    last_name = forms.CharField(
        label = "Apellidos",
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"Apellidos" 
            }
        )
    )
    
    cargo = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"Cargo"
            }
        )
    )
    edad = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class":"form-control",
                "step":1,
                "placeholder":"Edad"
            }
        )
    )
    sexo = forms.ChoiceField(
        choices=SEXO,
        label= "Sexo",
        widget=forms.RadioSelect(
            attrs={
                "class":"form-check form-check-inline",
            }
        )
    )

    class Meta:
        model = User
        fields = ('username','email','password1','password2','first_name','last_name','empresa','cargo','edad','sexo')
        labels = {'empresa':"Empresa"}
        widgets = {
            'empresa':forms.Select(attrs={'class':'form-selected',"placeholder":"Empresa","required":""})
        }
        
        