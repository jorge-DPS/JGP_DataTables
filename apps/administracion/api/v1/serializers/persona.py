from rest_framework import serializers
from apps.administracion.models import (Persona)

class PersonaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = (
            "primer_nombre",
            "segundo_nombre",
            "primer_apellido",
            "segundo_apellido",
            "apellido_esposo",
            "valor_documento_identificacion",
            "complemento",
            "extension",
            "usuario_actualizacion",
            "sucursal_creacion",
            "creado_en",
            "actualizado_en",
            "eliminado_en",
        )
class PersonaListarSerializer(serializers.ModelSerializer):
    text = serializers.SerializerMethodField()

    def get_text(self, obj):
        return obj.primer_nombre

    class Meta:
        model = Persona
        fields = (
            "id",
            "text",
            
        )
        
class PersonaAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = (
            "primer_nombre",
            "segundo_nombre",
            "primer_apellido",
            "segundo_apellido",
            "apellido_esposo",
            "valor_documento_identificacion",
            "complemento",
            "extension",
            "usuario_actualizacion",
            "sucursal_creacion",
            "creado_en",
            "actualizado_en",
            "eliminado_en",
        )
class PersonaEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = (
            "id",
            "primer_nombre",
            "segundo_nombre",
            "primer_apellido",
            "segundo_apellido",
            "apellido_esposo",
            "valor_documento_identificacion",
            "complemento",
            "extension",
            "usuario_actualizacion",
            "sucursal_creacion",
            "creado_en",
            "actualizado_en",
            "eliminado_en",
        )
class PersonaAddEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = (
            "id",
            "primer_nombre",
            "segundo_nombre",
            "primer_apellido",
            "segundo_apellido",
            "apellido_esposo",
            "valor_documento_identificacion",
            "complemento",
            "extension",
            "usuario_actualizacion",
            "sucursal_creacion",
            "creado_en",
            "actualizado_en",
            "eliminado_en",
        )