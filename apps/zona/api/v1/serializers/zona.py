from rest_framework import serializers
from apps.zona.models import Zona
from apps.zona.models import Localidad

class LocalidadListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Localidad
        fields = (
            'id',
            'descripcion', 
            'codigo_departamento',
            'codigo_localidad'
        )


class ZonaDetailSerializer(serializers.ModelSerializer):
    
    localidad=LocalidadListSerializer()
    class Meta:
        model = Zona
        
        fields = (
            'id',
            'descripcion',
            'localidad',
            'usuario_actualizacion',
            'sucursal_creacion',
        )
        
class ZonaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zona
        
        fields = (
            'id',
            'descripcion',
            'localidad',
            'usuario_actualizacion',
            'sucursal_creacion',
        )

class ZonaListSerializerLog(serializers.ModelSerializer):
    
    class Meta:
        model = Zona
        fields = (
            'id',
            'descripcion',
            'localidad',
            'usuario_actualizacion',
            'sucursal_creacion',
            'creado_en',
            'actualizado_en',
            'eliminado_en',
        )
