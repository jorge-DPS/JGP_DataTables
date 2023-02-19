# Django
from django.contrib import admin

# Models
from apps.empresa.models import Sucursal, Rol

@admin.register(Sucursal)
class SucursalAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "slug",
        "nombre",
        "direccion",
        "telefono",
        "foto",
        "punto_gps",
    )


@admin.register(Rol)
class RolAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "slug",
        "codigo",
        "nombre",
        "descripcion",
    )
    
