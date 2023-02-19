# Django
from django.contrib import admin

# Models
from apps.zona.models import Localidad


@admin.register(Localidad)
class LocalidadAdmin(admin.ModelAdmin):

    list_display = (
        'descripcion',
        'codigo_departamento',
        'codigo_localidad',
        'usuario_actualizacion',
        'sucursal_creacion',
        'creado_en',
        'actualizado_en',
        'eliminado_en',
    )


