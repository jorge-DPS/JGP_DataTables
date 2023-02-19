from logging import PlaceHolder

from django.forms import ModelForm
from apps.zona.models import Zona

from django import forms
from django.forms import TextInput, EmailInput

class ZonaForm(ModelForm):
    class Meta:
        model = Zona
        fields =[
            'descripcion',
            'localidad',
            'usuario_actualizacion',
            'sucursal_creacion',
            
            
            
        ]
        labels = {
            'descripcion': 'Nombre de zona',
            'localidad': 'localidad',
            
        }
        
        
        