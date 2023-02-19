from rest_framework import serializers
from apps.grupo.models import Grupo

class GrupoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grupo
        fields = (
            'codigo_grupo',
            'descripcion_grupo',
            'secuencia_grupo',
            'ultima_operacion',
            'usuario_actualizacion',
            'sucursal_creacion',
            'creado_en',
            'actualizado_en',
            'eliminado_en',
        )

