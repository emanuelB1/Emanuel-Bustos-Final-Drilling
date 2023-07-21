from django import forms
from .models import Laboratorio

class LaboratorioForm(forms.ModelForm):
    class Meta:
        model = Laboratorio
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Ingresar el Nombre del Laboratorio'}),
            'ciudad': forms.TextInput(attrs={'placeholder': 'Ingresar la Ciudad del laboratorio'}),
            'pais': forms.TextInput(attrs={'placeholder': 'Ingresar el Pais del laboratorio'}),
        }
