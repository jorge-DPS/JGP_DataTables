from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.mixins import PermissionRequiredMixin
from apps.contrib.api.viewsets import (ModelCreateListViewSet, 
                                        ModelRetrieveUpdateListViewSet, PermissionlMixin)
from apps.zona.api.v1.serializers.zona import ZonaListSerializerLog, ZonaDetailSerializer
from apps.zona.models.zona import Zona
from datetime import date, time, datetime

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

class ZonaViewSet(ModelCreateListViewSet,LogMixin,PermissionlMixin):
    permission_classes = [IsAuthenticated]
    #permission_required = ("zona.view_zona","zona.add_zona")
    serializer_class = ZonaDetailSerializer
    #permission_denied_message = 'no esta autorizado'
    
    def list(self, request, *args, **kwargs):
        zona = Zona.objects.filter(eliminado_en=None)
        return Response(self.get_serializer(zona, many=True).data, status=status.HTTP_200_OK)
        #return super(ZonaViewSet, self).list(request, *args, **kwargs)
    
    def get_queryset(self):
        queryset = Zona.objects.filter(eliminado_en=None)   
        return queryset
    
    def create(self, request, *args, **kwargs):
        #data._mutable=True
        data=self.load_logs()
        data['creado_en']=self.now_fecha()
        serializer = ZonaListSerializerLog(data=data)
        serializer.is_valid(raise_exception=True)
        zona = serializer.create(serializer.validated_data)
        return Response(self.get_serializer(zona).data, status=status.HTTP_201_CREATED)
        
    
class ZonasViewSet(ModelRetrieveUpdateListViewSet,LogMixin, PermissionRequiredMixin):
    permission_classes = [IsAuthenticated]
    #permission_required = ("zona.change_caja","zona.delete_zona")
    model= Zona
    serializer_class = ZonaDetailSerializer
    queryset=Zona.objects.all()

    def retrieve(self, request, *args, **kwargs):
        try:
            print("Detalles del id :============== ",kwargs["id"])
            zona_detalle = Zona.objects.get(id=kwargs["id"])
            if(zona_detalle.eliminado_en is None):
                zona_serializer=self.serializer_class(zona_detalle)
                return Response(zona_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({"message":"Este registro esta eliminado"})
        except Zona.DoesNotExist:
            return Response({'message':'No existe el registro '},status=status.HTTP_204_NO_CONTENT)      

    def delete(self, request, *args, **kwargs):
        try:
            print("eliminando un  Zona")
            eliminarZona = Zona.objects.get(id=kwargs["id"])
            eliminarZona.eliminado_en=self.now_fecha()
            eliminarZona.save()
            return Response({'message':'Se elimino corectamente'}, status=status.HTTP_204_NO_CONTENT)
        except Zona.DoesNotExist:
            return Response({'message':'No existe el registro '},status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        try: 
            zona = Zona.objects.get(id=kwargs["id"])
            if(zona.eliminado_en is None):
                data=self.request.data
                data=self.load_logs() 
                zona.actualizado_en=self.now_fecha()
                serializer = ZonaListSerializerLog(zona,data=request.data, partial=True)
                serializer.is_valid(raise_exception=True)
                _zona=serializer.save()
                return Response(ZonaListSerializerLog(_zona).data, status=status.HTTP_201_CREATED)
            else:
                return Response({"message":"No se puede editar este registro esta eliminado"})
        except Zona.DoesNotExist:
            return Response({'message':'No existe el registro '},status=status.HTTP_204_NO_CONTENT)

    