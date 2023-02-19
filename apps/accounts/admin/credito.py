# Django
from django.contrib import admin

# Models
from apps.credito.models import (EvaluacionEconomica,
                                Venta,Compra,
                                GastoOperativoMes,
                                GastoFamiliarMes,
                                ObligacionMes,
                                OtroIngreso,
                                Pendiente)

@admin.register(Pendiente)
class PendienteAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'evaluacion_id',
        'edad',
        'genero',
        'nivel_estudio',
        'usuario_actualizacion',
        'sucursal_creacion',
        'creado_en',
        'actualizado_en',
        'eliminado_en',   
    )

@admin.register(OtroIngreso)
class OtroIngresoAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'evaluacion_id',
        'conyugue',
        'otro_negocio',
        'rentas',
        'otro_ingresos',
        'usuario_actualizacion',
        'sucursal_creacion',
        'creado_en',
        'actualizado_en',
        'eliminado_en',   
          
    )

@admin.register(ObligacionMes)
class ObligacionMesAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'evaluacion_id',
        'detalle',
        'saldo_deudor',
        'cuota_mes',
        'usuario_actualizacion',
        'sucursal_creacion',
        'creado_en',
        'actualizado_en',
        'eliminado_en', 
    )

@admin.register(GastoFamiliarMes)
class GastoFamiliarMesAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'evaluacion_id',
        'alimentacion',
        'vivienda',
        'electricidad',
        'agua',
        'educacion',
        'transporte',
        'salud',
        'vestuario',
        'telefono',
        'recreacion',
        'otros',
        'usuario_actualizacion',
        'sucursal_creacion',
        'creado_en',
        'actualizado_en',
        'eliminado_en',   
    )

@admin.register(GastoOperativoMes)
class GastoOperativoAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'evaluacion_id',
        'alquileres',
        'agua',
        'electricidad',
        'telefono',
        'impuesto',
        'transporte',
        'salarios',
        'mantenimiento',
        'reparaciones',
        'otros',
        'usuario_actualizacion',
        'sucursal_creacion',
        'creado_en',
        'actualizado_en',
        'eliminado_en',   
    )

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'evaluacion_id',
        'producto_servicio',
        'unidad_venta',
        'cantidad_venta',
        'precio_venta',
        'frecuencia_venta',
        'ventas_mes',
        'usuario_actualizacion',
        'sucursal_creacion',
        'creado_en',
        'actualizado_en',
        'eliminado_en',   
    )
    
@admin.register(Compra)
class Compradmin(admin.ModelAdmin):

    list_display = (
        'id',
        'evaluacion_id',
        'producto_insumo',
        'unidad_compra',
        'cantidad_compra',
        'precio_compra',
        'frecuencia_compra',
        'compras_mes',
        'usuario_actualizacion',
        'sucursal_creacion',
        'creado_en',
        'actualizado_en',
        'eliminado_en',   
    )
    

    
    
    
    
#model para evaluacion economica
@admin.register(EvaluacionEconomica)
class EvaluacionEconomicaAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'persona_id',
        'actividad_evaluada',
        'actividad_principal',
        'ciclo_rotacion',
        'compra_aproximada_mensuales',
        'ventas_aproximada_lunes',
        'ventas_aproximada_martes',
        'ventas_aproximada_miercoles',
        'ventas_aproximada_jueves',
        'ventas_aproximada_viernes',
        'ventas_aproximada_sabado',
        'ventas_aproximada_domingo',
        'ventas_aproximada_mensuales',
        'numero_dependiente',
        'venta_elegida',
        'compras',
        'utilidad_bruta',
        'margen_utilidad_bruta',
        'usuario_actualizacion',
        'sucursal_creacion',
        'creado_en',
        'actualizado_en',
        'eliminado_en',   
    )