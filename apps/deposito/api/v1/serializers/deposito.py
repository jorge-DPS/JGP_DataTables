from rest_framework import serializers
from apps.deposito.models import Deposito

class DepositoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposito
        fields = (
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

