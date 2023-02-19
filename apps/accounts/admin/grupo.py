from django.contrib import admin

from apps.grupo.models import Grupo
#model para Grupo
@admin.register(Grupo)
class GrupoAdmin(admin.ModelAdmin):

    list_display = (
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
