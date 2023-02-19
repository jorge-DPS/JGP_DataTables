from multiprocessing.sharedctypes import RawValue
from ssl import ALERT_DESCRIPTION_UNEXPECTED_MESSAGE
from rest_framework import serializers

from apps.cajas.models import (Caja)

class CajaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caja
        fields = [
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
        ]
class CajaAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caja
        fields = [
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
        ] 
class CajaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caja
        fields = [
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
        ]  