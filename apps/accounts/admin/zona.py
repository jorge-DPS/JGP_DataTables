# Django
from django.contrib import admin

# Models
from apps.zona.models import Localidad, Zona

#model para zona
@admin.register(Localidad)
class LocalidadAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        'descripcion',
        'codigo_departamento',
        'codigo_localidad',
        'usuario_actualizacion',
        'sucursal_creacion',
        'creado_en',
        'actualizado_en',
        'eliminado_en',
    )
@admin.register(Zona)
class ZonaAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        'descripcion',
        'localidad',
        'usuario_actualizacion',
        'sucursal_creacion',
        'creado_en',
        'actualizado_en',
        'eliminado_en',
    )
