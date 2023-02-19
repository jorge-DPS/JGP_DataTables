# Django
from django.contrib import admin

# Models
from apps.administracion.models import Persona
#from apps.administracion.models.arqueo import CorteMoneda

#model para arqueo
@admin.register(Persona)
class AdministracionAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'primer_nombre',
        'segundo_nombre',
        'primer_apellido',
        'segundo_apellido',
        'apellido_esposo',
        'valor_documento_identificacion',
        'complemento',
        'extension',
        'usuario_actualizacion',
        'sucursal_creacion',
        'creado_en',
        'actualizado_en',
        'eliminado_en',
    )

