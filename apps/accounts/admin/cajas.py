# Django
from django.contrib import admin

# Models
from apps.cajas.models import Caja


#model para Caja
@admin.register(Caja)
class CajaAdmin(admin.ModelAdmin):

    list_display = (
        'descripcion_caja',
        'codigo_oficina',
        'saldo_minimo_mn',
        'saldo_maximo_mn',
        'saldo_minimo_me',
        'saldo_maximo_me',
        'saldo_minimo_mr',
        'saldo_maximo_mr',
        'codigo_usuario',
        'ultima_apertura',
        'ultimo_cuadre',
        'habilitada',
        'saldo_mn',
        'saldo_me',
        'saldo_mr',
        'estado_caja',
        'usuario_actualizacion',
        'sucursal_creacion',
        'creado_en',
        'actualizado_en',
        'eliminado_en',
    )