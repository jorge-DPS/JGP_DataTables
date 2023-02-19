from typing_extensions import Self
from urllib import request, response
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from apps.contrib.api.viewsets import ModelCreateListViewSet
from django.contrib.auth.mixins import PermissionRequiredMixin
from apps.contrib.api.viewsets import (ModelCreateListViewSet,
                                        ModelRetrieveUpdateListViewSet, PermissionlMixin)
from apps.deposito.api.v1.serializers.deposito import DepositoListSerializer
from apps.deposito.models.deposito import Deposito
from datetime import date, time, datetime

class LogMixin(object):
    def load_logs(self):
        data=self.request.data
        print(self.request.user.pk)
        data['usuario_actualizacion']=self.request.user.pk
        data['sucursal_creacion']=self.request.user.branch_office.pk
        return data
    def now_fecha(self):
        tiempo = datetime.now()
        fechahora = tiempo.replace(microsecond=0)
        data=fechahora
        return data
 
class DepositosViewSet(ModelCreateListViewSet,LogMixin,PermissionlMixin):
    permission_classes = [IsAuthenticated]
    #permission_required = ("deposito.view_deposito","deposito.add_deposito")
    model= Deposito
    serializer_class = DepositoListSerializer
    #permission_denied_message = 'no esta autorizado'
    def get_queryset(self):
        queryset=Deposito.objects.filter(eliminado_en=None)   
        return queryset
    
    def list(self, request, *args, **kwargs):
        deposito = Deposito.objects.filter(eliminado_en=None)
        return Response(self.get_serializer(deposito, many=True).data, status=status.HTTP_200_OK)
    
    deposito = DepositoListSerializer(many=True)
    class Meta:
        model = Deposito
        fields = "__all__"
        
    def create(self,data):
        #data=self.request.data
        print("===============><",self.request.user.pk)
        serializer = DepositoListSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.create(serializer.validated_data)
        return serializer.data   
         
    def save_array_deposito(self, request):
        print("=========",type(request.data))
        _depositos=[]
        if request.data["depositos"]:
            for deposito in request.data["depositos"]:
                if not Deposito.objects.filter(numero_transaccion=deposito['numero_transaccion']).exists():
                    deposito['creado_en']=self.now_fecha()
                    deposito['usuario_actualizacion']=self.request.user.pk
                    deposito['sucursal_creacion']=self.request.user.branch_office.pk
                    new_deposito=self.create(deposito)
                    _depositos.append(new_deposito)
                else:
                    print("este registro no se registro ya existe")
                    Response({"Mensaje":"Este registro ya existe"})
            return Response(_depositos,status=status.HTTP_200_OK)
        else:
            data_error={
                "message":"No se ha guardado el array de depositos"
            }
            return Response(data_error,status=status.HTTP_204_NO_CONTENT)
    
        
class DepositoViewSet(ModelRetrieveUpdateListViewSet,LogMixin, PermissionRequiredMixin):
    permission_classes = [IsAuthenticated]
    model= Deposito
    serializer_class = DepositoListSerializer
    queryset=Deposito.objects.all()
    def retrieve(self, request, *args, **kwargs):
        try:
            deposito_detalle = Deposito.objects.get(id=kwargs["id"])
            if(deposito_detalle.eliminado_en is None):
                deposito_serializer=self.serializer_class(deposito_detalle)
                return Response(deposito_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({"Mensaje":"Este registro esta eliminado"})
        except Deposito.DoesNotExist:
            return Response({'message':'No existe el registro '},status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, *args, **kwargs):
        try:   
            print("eliminando un  Deposito")
            eliminardeposito = Deposito.objects.get(id=kwargs["id"])
            eliminardeposito.eliminado_en=self.now_fecha()
            eliminardeposito.save()
            return Response({'message':'Se elimino corectamente'}, status=status.HTTP_204_NO_CONTENT)
        except Deposito.DoesNotExist:
            return Response({'message':'No existe el registro '},status=status.HTTP_204_NO_CONTENT)
    
    def update(self, request, *args, **kwargs):
        try:
            deposito = Deposito.objects.get(id=kwargs["id"])
            if(deposito.eliminado_en is None):
                data=self.request.data
                data=self.load_logs() 
                deposito.actualizado_en=self.now_fecha()
                serializer = DepositoListSerializer(deposito,data=request.data, partial=True)
                serializer.is_valid(raise_exception=True)
                _deposito=serializer.save()
                return Response(DepositoListSerializer(_deposito).data, status=status.HTTP_201_CREATED)
            else:
                return Response({"message":"No se puede editar este registro esta eliminado"})
            
        except Deposito.DoesNotExist:
            return Response({'message':'No existe el registro '},status=status.HTTP_204_NO_CONTENT)
         