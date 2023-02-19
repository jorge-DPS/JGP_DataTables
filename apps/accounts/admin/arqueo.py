# Django
from django.contrib import admin

# Models
from apps.cajas.models import TransaccionInventario,EncabezadoArqueo,DetalleArqueo,CorteMoneda,CuentasPorCobrar
#from apps.cajas.models.arqueo import CorteMoneda

#model para arqueo
@admin.register(TransaccionInventario)
class ArqueoAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'caja_id',
        'fecha_transaccion',
        'producto_financiero_id',
        'detalle',
        'fondo',
        'monto_ingreso',
        'monto_salida',
        'usuario_actualizacion',
        'sucursal_creacion',
        'creado_en',
        'actualizado_en',
        'eliminado_en',
    )


#model para arqueo
@admin.register(CuentasPorCobrar)
class ArqueoAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'caja_id',
        'funcionario_id',
        'fecha_entrega',
        'monto_entregado',
        'monto_devuelto',
        'monto_saldo',
        'fecha_ultimo_pago',
        'estado',
        'usuario_actualizacion',
        'sucursal_creacion',
        'creado_en',
        'actualizado_en',
        'eliminado_en',
    )


#model para arqueo
@admin.register(EncabezadoArqueo)
class ArqueoAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'caja_id',
        'usuario_id',
        'fecha_arqueo',
        'total_arqueo_mn',
        'total_arqueo_me',
        'observaciones',
        'arqueo_definitivo',
        'usuario_actualizacion',
        'sucursal_creacion',
        'creado_en',
        'actualizado_en',
        'eliminado_en',
    )



#model para detalle arqueo
@admin.register(DetalleArqueo)
class ArqueoDetalleAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'arqueo_id',
        'corte_moneda_id',
        'moneda_id',
        'cantidad_corte_moneda',
        'valor_corte_moneda',
        'usuario_actualizacion',
        'sucursal_creacion',
        'creado_en',
        'actualizado_en',
        'eliminado_en',
    )
# Models

@admin.register(CorteMoneda)
class CorteMonedaAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'moneda_id',
        'descripcion_corte_moneda',
        'valor_corte_moneda',
        'usuario_actualizacion',
        'sucursal_creacion',
        'creado_en',
        'actualizado_en',
        'eliminado_en',
    )
