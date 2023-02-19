from multiprocessing.sharedctypes import RawValue
from ssl import ALERT_DESCRIPTION_UNEXPECTED_MESSAGE
from rest_framework import serializers
from apps.procesos.arqueo.models import (Caja,EncabezadoArqueo,DetalleArqueo,
                                    MovimientoDia,SaldoProducto,CuentasRendir)
from apps.accounts.models.user import User

class CajaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caja
        fields = [
            'id',
            'codigo_caja',
            'descripcion',
            'sucursal',
        ]
class EncabezadoArqueoSerializer(serializers.ModelSerializer):
    cajero = User(many=True)
    caja = Caja(many=True)
    class Meta:
        model = EncabezadoArqueo
        fields = [
            'id',
            'cajero',
            'caja',
            'fecha',
            'total_sistema_a',
            'total_sistema_b',
            'total_material_monetario_mn',
            'total_material_monetario_me',
        ]
class DetalleArqueoSerializer(serializers.ModelSerializer):
    encabezado = EncabezadoArqueo(many=True)
    class Meta:
        model = DetalleArqueo
        fields = [
            'id',
            'encabezado',
            'tipo_moneda',
            'corte',
            'cantidad',
            'total',
        ]
class MovimientoDiaSerializer(serializers.ModelSerializer):
    encabezado = EncabezadoArqueo(many=True)
    caja = Caja(many=True)
    class Meta:
        model = MovimientoDia
        fields = [
            'encabezado'
            'caja',
            'codigo_producto_financiero',
            'detalle',
            'tipo_movimiento',
            'monto_a',
            'monto_b',
            'fecha_proceso_movimiento',
        ]         
class SaldoProductoSerializer(serializers.ModelSerializer):
    caja = Caja(many=True)
    class Meta:
        model = SaldoProducto
        fields = [
            'caja',
            'codigo_producto_financiero_saldo',
            'saldo_sistema_a',
            'saldo_sistema_b',
            'fecha_proceso',
        ]
class CuentasRendirSerializer(serializers.ModelSerializer):
    caja = Caja(many=True)
    class Meta:
        model = CuentasRendir
        fields = [
            'caja',
            'fecha_transaccion',
            'monto_entregado',
            'monto_recuperado',
            'saldo',
            'estado',
        ]        
