from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from apps.contrib.api.viewsets import ModelCreateListViewSet
from django.contrib.auth.mixins import PermissionRequiredMixin
from apps.contrib.api.viewsets import (ModelCreateListViewSet, 
                                        ModelRetrieveUpdateListViewSet, PermissionlMixin)
from apps.cajas.api.v1.serializers.corte_moneda import CorteMonedaListSerializer ,CorteMonedaFilterSerializer
from apps.cajas.models import CorteMoneda
from datetime import date, time, datetime

from rest_framework import filters
from rest_framework import generics

class FilterCorteMoneda(generics.ListAPIView):
    queryset = CorteMoneda.objects.all()
    serializer_class = CorteMonedaFilterSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['moneda_id']
    
    
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

class CortesViewSet(ModelCreateListViewSet,LogMixin,PermissionlMixin):
    permission_classes = [IsAuthenticated]
    #permission_required = ("corte_moneda.view_zona","corte_moneda.add_zona")
    serializer_class = CorteMonedaListSerializer
    #permission_denied_message = 'no esta autorizado'
    
    def list(self, request, *args, **kwargs):
        corte_moneda = CorteMoneda.objects.filter(eliminado_en=None)
        return Response(self.get_serializer(corte_moneda, many=True).data, status=status.HTTP_200_OK)
        #return super(ZonaViewSet, self).list(request, *args, **kwargs)
    
    def get_queryset(self):
        queryset = CorteMoneda.objects.filter(eliminado_en=None)   
        return queryset
    
    
    def create(self, request, *args, **kwargs):
        #data._mutable=True
        data=self.load_logs()
        data['creado_en']=self.now_fecha()
        serializer = CorteMonedaListSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        corte_moneda = serializer.create(serializer.validated_data)
        return Response(self.get_serializer(corte_moneda).data, status=status.HTTP_201_CREATED)
        
    
class CorteViewSet(ModelRetrieveUpdateListViewSet,LogMixin, PermissionRequiredMixin):
    permission_classes = [IsAuthenticated]
    #permission_required = ("corte_moneda.change_caja","corte_moneda.delete_zona")
    model= CorteMoneda
    serializer_class = CorteMonedaListSerializer
    
    def retrieve(self, request, *args, **kwargs):
        try:
            print("Detalles del id :============== ",kwargs["id"])
            zona_detalle = CorteMoneda.objects.get(id=kwargs["id"])
            if(zona_detalle.eliminado_en is None):
                zona_serializer=self.serializer_class(zona_detalle)
                return Response(zona_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({"message":"Este registro esta eliminado"})
        except CorteMoneda.DoesNotExist:
            return Response({'message':'No existe el registro '},status=status.HTTP_204_NO_CONTENT)      

    def delete(self, request, *args, **kwargs):
        try:
            print("eliminando un  CorteMoneda")
            eliminarZona = CorteMoneda.objects.get(id=kwargs["id"])
            eliminarZona.eliminado_en=self.now_fecha()
            eliminarZona.save()
            return Response({'message':'Se elimino corectamente'}, status=status.HTTP_204_NO_CONTENT)
        except CorteMoneda.DoesNotExist:
            return Response({'message':'No existe el registro '},status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        try: 
            corte_moneda = CorteMoneda.objects.get(id=kwargs["id"])
            if(corte_moneda.eliminado_en is None):
                data=self.request.data
                data=self.load_logs() 
                corte_moneda.actualizado_en=self.now_fecha()
                serializer = CorteMonedaListSerializer(corte_moneda,data=request.data, partial=True)
                serializer.is_valid(raise_exception=True)
                _moneda=serializer.save()
                return Response(CorteMonedaListSerializer(_moneda).data, status=status.HTTP_201_CREATED)
            else:
                return Response({"message":"No se puede editar este registro esta eliminado"})
            
        except CorteMoneda.DoesNotExist:
            return Response({'message':'No existe el registro '},status=status.HTTP_204_NO_CONTENT)

    