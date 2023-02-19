from apps.contrib.api.viewsets import ModelCreateListViewSet
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response

from apps.empresa.api.v1.serializers.sucursal import SucursalListSerializer
from apps.empresa.models import Sucursal

class SucursalListView(ModelCreateListViewSet):
    serializer_class = SucursalListSerializer

    def get_queryset(self):
        return Sucursal.objects.all().order_by('-id')
    
    def list(self, request, *args, **kwargs):
        print("***********CARGANDO SUCURSALES***********")
        sucursales = Sucursal.objects.all().order_by('-id')
        
        return Response(SucursalListSerializer(sucursales, many=True).data, status=status.HTTP_200_OK)
