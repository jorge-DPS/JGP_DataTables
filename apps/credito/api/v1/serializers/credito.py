from dataclasses import fields
from multiprocessing.sharedctypes import RawValue
from ssl import ALERT_DESCRIPTION_UNEXPECTED_MESSAGE
from rest_framework import serializers
from apps.credito.models import (EvaluacionEconomica,
                                Venta,Compra,
                                GastoOperativoMes,
                                GastoFamiliarMes,
                                ObligacionMes,
                                OtroIngreso,
                                Pendiente)
from datetime import datetime



#==================================Pendiente========================== 
class CreadosPendientes(serializers.ListSerializer):
    def to_representation(self,data):
        data = data.filter(eliminado_en = None)
        return super(CreadosPendientes, self).to_representation(data)   
 
class PendienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pendiente
        list_serializer_class=CreadosPendientes
        fields = [
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
        ]
        read_only_fields=('eliminado_en',)
#==================================OtroIngreso==========================  
class CreadosIngreso(serializers.ListSerializer):
    def to_representation(self,data):
        data = data.filter(eliminado_en = None)
        return super(CreadosIngreso, self).to_representation(data)   
             
class OtroIngresoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtroIngreso
        list_serializer_class=CreadosIngreso
        fields = [
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
        ]
        read_only_fields=('eliminado_en',)
#==================================ObligacionMes==========================  
class CreadosObligacion(serializers.ListSerializer):
    def to_representation(self,data):
        data = data.filter(eliminado_en = None)
        return super(CreadosObligacion, self).to_representation(data)   
       
class ObligacionMesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObligacionMes
        list_serializer_class=CreadosObligacion
        fields = [
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
        ]
        read_only_fields=('eliminado_en',)
#==================================GastoFamiliarMes==========================  
class CreadosFamiliar(serializers.ListSerializer):
    def to_representation(self,data):
        data = data.filter(eliminado_en = None)
        return super(CreadosFamiliar, self).to_representation(data)
        
class GastoFamiliarMesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GastoFamiliarMes
        list_serializer_class=CreadosFamiliar
        fields = [
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
        ]
        read_only_fields=('eliminado_en',)
#==================================GastoOperativoMes==========================   
class CreadosOperativo(serializers.ListSerializer):
    def to_representation(self,data):
        data = data.filter(eliminado_en = None)
        return super(CreadosOperativo, self).to_representation(data)
            
class GastoOperativoMesMesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GastoOperativoMes
        list_serializer_class=CreadosOperativo
        fields = [
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
        ]
        read_only_fields=('eliminado_en',)
#==================================Compra==========================   
class ActualizadoCompra(serializers.ListSerializer):
    def to_representation(self,data):
        data = data.filter(eliminado_en = None)
        return super(ActualizadoCompra, self).to_representation(data)
       
class CompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compra
        list_serializer_class=ActualizadoCompra
        fields = [
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
        ]
        read_only_fields=('eliminado_en',)

#==================================Venta==========================    
class ActualizadoVentas(serializers.ListSerializer):
    def to_representation(self,data):
        data = data.filter(eliminado_en = None)
        return super(ActualizadoVentas, self).to_representation(data)
    
class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        list_serializer_class=ActualizadoVentas
        fields = (
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
        read_only_fields=('eliminado_en',)

#==================================EvaluacionEconomica==========================        
class EvaluacionEconomicaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = EvaluacionEconomica
        fields = [
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
            
        ]    
#==================================EvaluacionEconomica Retrieve==========================        
class EvaluacionEconomicaRetrieveSerializer(serializers.ModelSerializer):
    
    venta_evaluacion_economica=VentaSerializer(many=True, read_only=True)
    compra_evaluacion_economica=CompraSerializer(many=True, read_only=True)
    gasto_operativo_evaluacion_economica=GastoOperativoMesMesSerializer(many=True, read_only=True)
    gasto_familiar_evaluacion_economica=GastoFamiliarMesSerializer(many=True, read_only=True)
    obligacion_evaluacion_economica=ObligacionMesSerializer(many=True, read_only=True)
    otro_ingreso_evaluacion_economica=OtroIngresoSerializer(many=True, read_only=True)
    pendiente_evaluacion_economica=PendienteSerializer(many=True, read_only=True)
    
    class Meta:
        model = EvaluacionEconomica
        fields = [
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
            
            
            'venta_evaluacion_economica',
            'compra_evaluacion_economica',
            'gasto_operativo_evaluacion_economica',
            'gasto_familiar_evaluacion_economica',
            'obligacion_evaluacion_economica',
            'otro_ingreso_evaluacion_economica',
            'pendiente_evaluacion_economica',
        ]        
        
        
        
