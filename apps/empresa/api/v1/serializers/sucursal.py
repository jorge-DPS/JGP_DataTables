from rest_framework import serializers
from apps.empresa.models import Sucursal

class SucursalListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursal
        fields = (
            "slug",
            "nombre",
            "direccion",
            "telefono",
            "foto",
            "punto_gps",
        )
