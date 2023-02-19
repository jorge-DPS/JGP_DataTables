
from dataclasses import fields
from multiprocessing.sharedctypes import RawValue
from ssl import ALERT_DESCRIPTION_UNEXPECTED_MESSAGE
from rest_framework import serializers
from apps.cajas.models import (CuentasPorCobrar,TransaccionInventario,EncabezadoArqueo,
                                    DetalleArqueo,CorteMoneda)
from apps.cajas.models import (Caja)
from apps.accounts.models import User
from apps.empresa.models import Sucursal
from datetime import datetime,timedelta

#==================================Corete Moneda========================== 
class CorteMonedaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CorteMoneda
        fields = (
            'id',
            'moneda_id',
            'descripcion_corte_moneda',
            'valor_corte_moneda',
        )

class CorteMonedaFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CorteMoneda
        fields = (
            'id',
            'moneda_id',
            'descripcion_corte_moneda',
            'valor_corte_moneda'
            
        )
#==================quita los elimados de la lista
class ActualizadoCuenta(serializers.ListSerializer):
    def to_representation(self,data):
        data = data.filter(eliminado_en = None)
        return super(ActualizadoCuenta, self).to_representation(data)
  
class CuentasPorCobrarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CuentasPorCobrar
        list_serializer_class=ActualizadoCuenta
        fields = [
            'codigo_caja',
            'codigo_funcionario',
            'fecha_entrega',
            'monto_entregado',
            'monto_devuelto',
            'monto_saldo',
            'ultima_fecha_pago',
            'estado',
            'usuario_actualizacion',
            'sucursal_creacion',
            'creado_en',
            'actualizado_en',
            'eliminado_en',
        ]
        read_only_fields=('eliminado_en',)

#==================================Detalle arqueo========================== 
class DetalleArqueoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleArqueo
        fields = [
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
        ]
        
class DetalleArqueoRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleArqueo
        fields = [
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
        ]
#==================================Encabezdo Arqueo========================== 
#===============================para arqueo con caja
class EncabezadoArqueoCajaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Caja
        
        fields = (
            'id',
            'descripcion_caja',
        )       
class EncabezadoArqueoSerializer(serializers.ModelSerializer):
    caja_id=EncabezadoArqueoCajaSerializer()
    class Meta:
        model = EncabezadoArqueo
        fields = [
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
        ]
#======================Serializer para encabezado con cajas
class EncabezadoArqueoPOSTSerializer(serializers.ModelSerializer):
    class Meta:
        model = EncabezadoArqueo
        fields = [
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
        ]
#para crear y listar un arqueo y sus detalles
class ArqueoDetailSerializer(serializers.ModelSerializer):
    
    detalle = DetalleArqueoSerializer(many=True, read_only=True)
    class Meta:
        model = EncabezadoArqueo
        
        fields = (
            'id',
            'caja_id',
            'usuario_id',
            'fecha_arqueo',
            'total_arqueo_mn',
            'total_arqueo_me',
            'detalle'
        )

class EncabezaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EncabezadoArqueo
        fields = (
            'id',
            'caja_id',
            'usuario_id',
            'fecha_arqueo',
            'total_arqueo_mn',
            'total_arqueo_me',
            
        )
#====================================encabezado enviando fecha d parametro
class ActualizadoEncabezado(serializers.ListSerializer):
    
    def retrievefecha(self,data):
        global fecha_busqueda
        fecha_busqueda=data
        
        return fecha_busqueda

    def to_representation(self,data):
        print("Dato global ",fecha_busqueda)
        fecha_inicio=fecha_busqueda
        fecha_fin=fecha_busqueda
        dia=1
        dt_obj_1=fecha_inicio-timedelta(dia,0)
        print("restado: ",dt_obj_1)

        dt_obj_2=fecha_fin+timedelta(dia,0)
        print("sumado: ",dt_obj_2)
        data = data.filter(eliminado_en = None).filter(fecha_arqueo__gte=dt_obj_1,fecha_arqueo__lte=dt_obj_2)
        return super(ActualizadoEncabezado, self).to_representation(data)
  
class EncabezaJnSerializer(serializers.ModelSerializer):
    caja_id=EncabezadoArqueoCajaSerializer()
    detalle_arqueo_encabezado=DetalleArqueoRetrieveSerializer(many=True)
    class Meta:
        model = EncabezadoArqueo
        list_serializer_class=ActualizadoEncabezado
        fields = (
            'id',
            'caja_id',
            'usuario_id',
            'fecha_arqueo',
            'total_arqueo_mn',
            'total_arqueo_me',
            'observaciones',
            'creado_en',
            'eliminado_en', 
            'detalle_arqueo_encabezado',

        )
        read_only_fields=('fecha_arqueo','eliminado_en',)
        
 #======================================================================       

class CuentasPorCobrarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CuentasPorCobrar
        fields = (
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
#==================================Cuentas por Cobrar Con User========================== 
class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'avatar',
            'birthdate',
            'phone',
            'incorporation_date',
        )
#==================================Cuentas por Cobrar METODO GET LISTAR Con User========================== 
class UserSerializer(serializers.ModelSerializer):
    nombre_completo=serializers.SerializerMethodField()
    
    def get_nombre_completo(self, obj):
        return f'{obj.first_name} {obj.last_name}'
    
    class Meta:
        model = User
        fields = (
            'id',
            'nombre_completo',        
        )

class ActualizadoCuenta(serializers.ListSerializer):
    def to_representation(self,data):
        data = data.filter(eliminado_en = None)
        return super(ActualizadoCuenta, self).to_representation(data)
  
class CuentasPorCobrarListarSerializer(serializers.ModelSerializer):
    funcionario_id=UserUpdateSerializer()
    class Meta:
        model = CuentasPorCobrar
        list_serializer_class=ActualizadoCuenta
        fields = (
            'id',
            'caja_id',
            'funcionario_id',
            'fecha_entrega',
            'monto_entregado',
            'monto_devuelto',
            'monto_saldo',
            'fecha_ultimo_pago',
            'estado',
            'eliminado_en'
        )
        read_only_fields=('eliminado_en',)
            #=================LISTA PARA EL METODO GET
class CuentasPorCobrarListarGETSerializer(serializers.ModelSerializer):
    funcionario_id=UserSerializer()
    class Meta:
        model = CuentasPorCobrar
        fields = (
            'id',
            'caja_id',
            'funcionario_id',
            'fecha_entrega',
            'monto_entregado',
            'monto_devuelto',
            'monto_saldo',
            'fecha_ultimo_pago',
            'estado',
        )
#====================transaccion Inventarios==========================
class TransaccionInventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransaccionInventario
        fields = (
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
#====================quita los elimicados
class ActualizadoInventario(serializers.ListSerializer):
    def inventaiofecha(self,data):
        global fecha_busqueda
        fecha_busqueda=data
        return fecha_busqueda

    def to_representation(self,data):
        print("Dato global ",fecha_busqueda)
        fecha_inicio=fecha_busqueda
        fecha_fin=fecha_busqueda
        dia=1
        dt_obj_1=fecha_inicio-timedelta(dia,0)
        print("restado: ",dt_obj_1)

        dt_obj_2=fecha_fin+timedelta(dia,0)
        print("sumado: ",dt_obj_2)
        data = data.filter(eliminado_en = None).filter(fecha_transaccion__gte=dt_obj_1,fecha_transaccion__lte=dt_obj_2)
        return super(ActualizadoInventario, self).to_representation(data)
  
class TransaccionInventarioListarSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TransaccionInventario
        list_serializer_class=ActualizadoInventario
        fields = (
            'id',
            'caja_id',
            'fecha_transaccion',
            'producto_financiero_id',
            'detalle',
            'fondo',
            'monto_ingreso',
            'monto_salida',
            'eliminado_en', 
            
        )        
        read_only_fields=('fecha_transaccion','eliminado_en',)

#==================================ARQUEO DETALLE INVENTARIO CUENTA==========================
#==========sucursal
class SucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursal
        fields = (
            "id",
            "slug",
            "nombre",
            "direccion",
            "telefono",
            "foto",
            "punto_gps",
        )
#==================================arqueo caja
class ArqueoCajaSerializer(serializers.ModelSerializer):
    codigo_oficina=SucursalSerializer()
    codigo_usuario=UserUpdateSerializer()
    codigo_caja_encabezadoarqueo=EncabezaJnSerializer(many=True, read_only=True)
    codigo_caja_transaccioninventario=TransaccionInventarioListarSerializer(many=True, read_only=True)
    codigo_caja_cuentasporcobrar=CuentasPorCobrarListarSerializer(many=True, read_only=True)

    class Meta:
        model = Caja
        
        fields = (
            'id',
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
            'codigo_caja_encabezadoarqueo',
            'codigo_caja_transaccioninventario',
            'codigo_caja_cuentasporcobrar'

        )
