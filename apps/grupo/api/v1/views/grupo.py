from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from apps.contrib.api.viewsets import ModelCreateListViewSet
from django.contrib.auth.mixins import PermissionRequiredMixin
from apps.contrib.api.viewsets import (ModelCreateListViewSet,
                                        ModelRetrieveUpdateListViewSet, PermissionlMixin)
from apps.grupo.api.v1.serializers.grupo import GrupoListSerializer
from apps.grupo.models.grupo import Grupo
from datetime import date, time, datetime

from django.http import Http404
from django.shortcuts import render
#from polls.models import Poll

class LogMixin(object):
    def load_logs(self):
        data=self.request.data
        data['usuario_actualizacion']=self.request.user.pk
        data['sucursal_creacion']=self.request.user.branch_office.pk
        return data
    def now_fecha(self):
        tiempo = datetime.now()
        fechahora = tiempo.replace(microsecond=0)
        data=fechahora
        return data

class GruposViewSet(ModelCreateListViewSet,LogMixin,PermissionlMixin):
    permission_classes = [IsAuthenticated]
    model= Grupo
    serializer_class = GrupoListSerializer
   
    def get_queryset(self):
        queryset = Grupo.objects.filter(eliminado_en=None)   
        return queryset
    
    def list(self, request, *args, **kwargs):
        grupos = Grupo.objects.filter(eliminado_en=None)
        return Response(self.get_serializer(grupos, many=True).data, status=status.HTTP_200_OK)
    
    def create(self, request, *args, **kwargs):
        #data._mutable=True
        data=self.load_logs()
        data['creado_en']=self.now_fecha()
        serializer = GrupoListSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        grupo = serializer.create(serializer.validated_data)
        return Response(self.get_serializer(grupo).data, status=status.HTTP_201_CREATED)
        
    
class GrupoViewSet(ModelRetrieveUpdateListViewSet,LogMixin, PermissionRequiredMixin):
    permission_classes = [IsAuthenticated]
    model= Grupo
    serializer_class = GrupoListSerializer
    queryset=Grupo.objects.all()
    def retrieve(self, request, *args, **kwargs):
        try:
            grupo_detalle = Grupo.objects.get(codigo_grupo=kwargs["codigo_grupo"])
            if(grupo_detalle.eliminado_en is None):
                grupo_serializer=self.serializer_class(grupo_detalle)
                return Response(grupo_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({"message":"Este registro esta eliminado"})
        
        except Grupo.DoesNotExist:
            return Response({'message':'No existe el registro '},status=status.HTTP_204_NO_CONTENT)
        
    def delete(self, request, *args, **kwargs):
        try:   
            print("eliminando un  Grupo")
            eliminarGrupo = Grupo.objects.get(codigo_grupo=kwargs["codigo_grupo"])
            eliminarGrupo.eliminado_en=self.now_fecha()
            eliminarGrupo.save()
            return Response({'message':'Se elimino corectamente'}, status=status.HTTP_204_NO_CONTENT)
        except Grupo.DoesNotExist:
            return Response({'message':'No existe el registro '},status=status.HTTP_204_NO_CONTENT)
    
    def update(self, request, *args, **kwargs):
        try: 
            grupo = Grupo.objects.get(codigo_grupo=kwargs["codigo_grupo"])
            if(grupo.eliminado_en is None):
                data=self.request.data
                data=self.load_logs() 
                grupo.actualizado_en=self.now_fecha()
                serializer = GrupoListSerializer(grupo,data=request.data, partial=True)
                serializer.is_valid(raise_exception=True)
                _grupo=serializer.save()
                return Response(GrupoListSerializer(_grupo).data, status=status.HTTP_201_CREATED)
            else:
                return Response({"message":"No se puede editar este registro esta eliminado"})
            
        except Grupo.DoesNotExist:
            return Response({'message':'No existe el registro '},status=status.HTTP_204_NO_CONTENT)

    
                             