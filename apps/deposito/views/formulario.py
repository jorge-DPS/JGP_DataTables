from django.forms import ModelForm
from apps.deposito.models import Deposito

from django import forms
from django.forms import TextInput, EmailInput

class DepositoForm(ModelForm):
    class Meta:
        model = Deposito
        fields =[
            'numero_cuenta',
            'fecha_deposito',
            'descripcion',
            'numero_transaccion',
            'monto_mn',
            'estado',
        ]
        labels = {
            'numero_cuenta':'Nuemro de cuenta',
            'fecha_deposito':'Fecha de deposito',
            'descripcion':'Descripcion grupo',
            'numero_transaccion':'Numero de tranferencia',
            'monto_mn':'Monto modeda nacional',
            'estado':'Estado de deposito',
            
            
        }