# Django
from django.contrib import admin

# Models
from apps.deposito.models import Deposito

#model para zona
@admin.register(Deposito)
class DepositoAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'numero_cuenta',
        'fecha_deposito',
        'descripcion',
        'numero_transaccion',
        'monto_mn',
        'estado',
        'usuario_actualizacion',
        'sucursal_creacion',
        'creado_en',
        'actualizado_en',
        'eliminado_en',   
    )