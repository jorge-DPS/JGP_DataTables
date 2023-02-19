from django.shortcuts import render
import requests, json
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveAPIView, GenericAPIView
from apps.contrib.api.exceptions import NotFound
from apps.contrib.api.viewsets import ModelCreateListViewSet,ModelRetrieveUpdateListViewSet
from apps.contrib.api.viewsets import PermissionViewSet
from apps.procesos.arqueo.models import Caja
from apps.procesos.arqueo.api.v1.serializers.caja import (CajaSerializer, EncabezadoArqueoSerializer,
MovimientoDiaSerializer,SaldoProductoSerializer,CuentasRendirSerializer,DetalleArqueoSerializer)


class CajaViewSet(PermissionViewSet,ModelCreateListViewSet):
    """Contains all caja endpoints."""
    serializer_class = CajaSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        return super(CajaViewSet, self).list(request, *args, **kwargs)

    def get_queryset(self):
        queryset = EncabezadoArqueoSerializer.objects.all()
        return queryset
    
class CajaCreateViewSet(PermissionViewSet, ModelCreateListViewSet):
    serializer_class = CajaSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        print("------------------ POST CAJA ------------------",request.data)
        serializer = CajaSerializer(data=request.data)
        print()
        print(serializer)
        print("")
        serializer.is_valid(raise_exception=True)
        caja = serializer.create(serializer.validated_data)

        return Response(CajaSerializer(caja).data, status=status.HTTP_201_CREATED)


class CajaDeleteViewSet(PermissionViewSet,ModelCreateListViewSet):
    """Contains all caja endpoints."""
    serializer_class = CajaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Caja.objects.all()
        return queryset
    
    def delete(self, request, **kwargs):
        print("------------------ DELETE CAJA ------------------",kwargs["pk"])
        caja = Caja.objects.get(id=kwargs["pk"])
        caja.save()
        return Response(CajaSerializer(caja).data, status=status.HTTP_201_CREATED)         

