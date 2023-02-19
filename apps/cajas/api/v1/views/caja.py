from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveAPIView, GenericAPIView
from apps.contrib.api.viewsets import ModelCreateListViewSet, ModelUpdateListViewSet, ModelRetrieveUpdateListViewSet
from apps.contrib.api.exceptions import NotFound
from apps.cajas.models import Caja
from apps.contrib.api.viewsets import ModelCreateListViewSet
from apps.contrib.api.viewsets import PermissionViewSet
from datetime import datetime
from apps.cajas.api.v1.serializers.caja import (CajaSerializer,CajaAddSerializer,CajaListSerializer)

class LogMixin(object):
    def load_logs(self):
        data=self.request.data
        data['usuario_actualizacion']=self.request.user.pk
        data['sucursal_creacion']=self.request.user.branch_office.pk
        return data
    def now_fecha(self):
        tiempo = datetime.now()
        fechahora = tiempo.replace(microsecond=0)
        #fechahora = tiempo.strftime("%Y/%m/%d %H:%M:%S")
        data=fechahora
        return data
class CajaViewSet(PermissionViewSet, ModelCreateListViewSet,LogMixin):
    """Contains all persona endpoints."""
    serializer_class = CajaListSerializer
    permission_classes = [IsAuthenticated]
    def list(self, request, *args, **kwargs):
        return super(CajaViewSet, self).list(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Caja.objects.filter(estado_caja="V")
        return queryset

    def create(self, request, *args, **kwargs):
        print("------------------ POST CAJA ------------------",request.data)
       
        #data._mutable=True
        print(self.get_permissions)
        data=self.load_logs()
        datavalida=data['descripcion_caja'].title().strip()  
        data['descripcion_caja']=" ".join(datavalida.split())
        data['creado_en']=self.now_fecha()
        serializer = CajaAddSerializer(data=data)
        print(serializer)
        is_valid = serializer.is_valid(raise_exception=True)
        if is_valid:
            caja = serializer.create(serializer.validated_data)
        else:
            return Response({'error': "No se pudo guardar la caja"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(CajaAddSerializer(caja).data, status=status.HTTP_201_CREATED) 

class CajaEditViewSet(IsAuthenticated, ModelRetrieveUpdateListViewSet,LogMixin):
    permission_classes = [IsAuthenticated]
    def update(self, request, *args, **kwargs):
        try:
            print("Actualizando datos de la Caja: ", kwargs["pk"])
            caja = Caja.objects.get(id=kwargs["pk"])
            data=self.request.data
            data=self.load_logs() 
            datavalida=data['descripcion_caja'].lower().capitalize()   
            data['descripcion_caja']=" ".join(datavalida.split())
            print("Actualizando Datos principales de la Caja", request.data)
            caja.actualizado_en=self.now_fecha()
            
            serializer = CajaAddSerializer(caja, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            _caja=serializer.save()
            return Response(CajaAddSerializer(_caja).data, status=status.HTTP_200_OK)
        except Exception:
            return Response({'message':'No existe el registro '},status=status.HTTP_204_NO_CONTENT)
    def retrieve(self, request, *args, **kwargs):
        try:
            caja = Caja.objects.get(id=kwargs["pk"])
            if(caja.eliminado_en is None):
                caja_serializer=self.serializer_class(caja)
                return Response(caja_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({"mensaje":"Este registro esta eliminado"})
        
        except Exception:
            return Response({'message':'No existe el registro '},status=status.HTTP_204_NO_CONTENT)
        
    def delete (self, request, *args, **kwargs):
        try:
            print("******************** Eliminando Caja: ", kwargs["pk"])
            caja = Caja.objects.get(pk=kwargs["pk"])
            caja.estado_caja = "B"
            caja.eliminado_en=self.now_fecha()
            caja.save()
            return Response(CajaAddSerializer(caja, many=False).data, status=status.HTTP_200_OK)
        except Exception:
            return Response({'message':'No existe el registro '},status=status.HTTP_204_NO_CONTENT)
         