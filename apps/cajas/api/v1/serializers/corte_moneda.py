from rest_framework import serializers
from apps.cajas.models import CorteMoneda

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